"""Compare fictional metadata. NOT SAML parsing, signature verification, or access authorization."""
import argparse
from datetime import datetime,timezone
import json
from pathlib import Path


def instant(value):
    if not isinstance(value,str):raise ValueError('timestamp string required')
    t=datetime.fromisoformat(value.replace('Z','+00:00'))
    if t.tzinfo is None or t.utcoffset() is None:raise ValueError('timezone required')
    return t.astimezone(timezone.utc)


def check(data,now='2026-11-01T11:00:00Z'):
    when=instant(now)
    if not isinstance(data,dict) or data.get('schema')!='training-claims-v1':raise ValueError('training schema required')
    policy=data['policy'];rows=data['records']
    if not isinstance(policy,dict) or any(not isinstance(policy.get(k),str) or not policy[k] for k in ('issuer','audience')):raise ValueError('policy values required')
    if not isinstance(rows,list) or not rows:raise ValueError('non-empty records required')
    seen=set();results=[]
    for row in rows:
        if not isinstance(row,dict) or any(not isinstance(row.get(k),str) or not row[k] for k in ('id','issuer','audience','not_before','not_on_or_after')):raise ValueError('record fields required')
        if row['id'] in seen:raise ValueError('duplicate record id')
        seen.add(row['id'])
        if type(row.get('fixture_signature_ok')) is not bool:raise ValueError('fixture boolean required')
        start,end=instant(row['not_before']),instant(row['not_on_or_after'])
        if start>=end:raise ValueError('start must precede end')
        reasons=[]
        if row['issuer']!=policy['issuer']:reasons.append('issuer_mismatch')
        if row['audience']!=policy['audience']:reasons.append('audience_mismatch')
        if not start<=when<end:reasons.append('outside_training_window')
        if not row['fixture_signature_ok']:reasons.append('fixture_reports_signature_failure')
        results.append(dict(id=row['id'],status='metadata_matches_training_policy' if not reasons else 'metadata_mismatch',reasons=reasons))
    return dict(now=when.isoformat(),results=results,signature_checks_performed=0,real_tokens_processed=0,access_decisions_performed=0,external_actions=0)


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('file',type=Path);p.add_argument('--now',default='2026-11-01T11:00:00Z');a=p.parse_args()
    try:
        print(json.dumps(check(json.loads(a.file.read_text(encoding='utf-8')),a.now),indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError,OverflowError) as exc:
        print('ERROR '+str(exc));return 2


if __name__=='__main__':raise SystemExit(main())
