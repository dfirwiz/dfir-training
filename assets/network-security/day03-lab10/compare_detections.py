"""Group original fictional detections and hash two benign reference texts, never scan samples."""
import json,sys
from pathlib import Path
from datetime import datetime

def stamp(s):
    if s is None:return None
    if not isinstance(s,str):raise ValueError('timestamp string or null required')
    t=datetime.fromisoformat(s.replace('Z','+00:00'))
    if t.utcoffset() is None:raise ValueError('timezone required')
    return t

def eq(a,b):return None if a is None or b is None else a==b

def all_claims(v):
    if False in v:return False
    return None if None in v else True

import hashlib,re
from collections import Counter

def compare(d,paths):
    if d.get('schema')!='training-detection-records-v1' or d.get('external_actions') is not False:raise ValueError('fictional contract required')
    if len(paths)!=2 or len({p.resolve() for p in paths})!=2:raise ValueError('two distinct reference files required')
    start=stamp(d['start']);end=stamp(d['end'])
    if start is None or end is None or start>=end:raise ValueError('ordered window required')
    references=[dict(name=p.name,bytes=len(p.read_bytes()),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths]
    hashes={x['sha256'] for x in references};seen={};window=[];unknown_time=[];duplicates=0
    for x in d['records']:
        if not isinstance(x['id'],str) or not x['id']:raise ValueError('id required')
        if x['id'] in seen:
            if x!=seen[x['id']]:raise ValueError('conflicting duplicate id')
            duplicates+=1;continue
        seen[x['id']]=x
        h=x['sha256_claim']
        if h is not None and (not isinstance(h,str) or re.fullmatch('[0-9a-f]{64}',h) is None):raise ValueError('lowercase sha256 or null required')
        for k in ('name_claim','label_claim'):
            if not isinstance(x[k],str) or not x[k]:raise ValueError('nonempty label/name required')
        if x['action_claim'] not in ('detected','quarantined','failed','unknown'):raise ValueError('invalid action')
        t=stamp(x['time'])
        if t is None:unknown_time.append(x['id'])
        elif start<=t<end:window.append(x)
    known={x['sha256_claim'] for x in window if x['sha256_claim'] is not None}
    return dict(input_rows=len(d['records']),duplicate_rows=duplicates,unique_record_ids=len(seen),in_window_records=len(window),unknown_time_ids=unknown_time,known_hash_groups=len(known),unknown_hash_records=sum(x['sha256_claim'] is None for x in window),label_counts=dict(Counter(x['label_claim'] for x in window)),action_claim_counts=dict(Counter(x['action_claim'] for x in window)),reference_files=references,reference_claim_matches=[dict(id=x['id'],matches=None if x['sha256_claim'] is None else x['sha256_claim'] in hashes) for x in window],external_actions=0,actual_antivirus_scan=False,actual_detection=False,actual_quarantine=False,incident_conclusion='unresolved')

if __name__=='__main__':
    print(json.dumps(compare(json.loads(Path(sys.argv[1]).read_text(encoding='utf-8')),[Path(p) for p in sys.argv[2:]]),ensure_ascii=False,indent=2))
