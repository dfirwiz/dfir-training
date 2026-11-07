"""Own offline claim comparison, not an OS application-control engine."""
import json,hashlib,sys
from pathlib import Path

def both(a,b):
    if a is False or b is False:return False
    return True if a is True and b is True else None

def compare(data,ref):
    if not isinstance(data,list):raise ValueError('cases must be a list')
    seen=set();out=[]
    for row in data:
        if not isinstance(row,dict) or set(row)!={'id','targeted','policy_applied','mode','sha256'}:raise ValueError('invalid fields')
        key=row['id']
        if not isinstance(key,str) or not key or key in seen:raise ValueError('invalid or duplicate id')
        seen.add(key)
        for field in ('targeted','policy_applied'):
            if row[field] is not None and type(row[field]) is not bool:raise ValueError('claim must be bool or null')
        if row['mode'] not in ('audit','enforce'):raise ValueError('unsupported mode')
        value=row['sha256']
        if value is not None and (not isinstance(value,str) or len(value)!=64 or any(c not in '0123456789abcdef' for c in value)):raise ValueError('expected lowercase SHA256 or null')
        coverage=both(row['targeted'],row['policy_applied'])
        match=(value==ref) if coverage is True and value is not None else None
        projection='unresolved'
        if match is True:projection='passes_this_hash_check'
        elif match is False:projection='would_block' if row['mode']=='audit' else 'block_if_model'
        out.append(dict(id=key,coverage_claim=coverage,hash_match=match,projection=projection))
    return out

if __name__=='__main__':
    try:
        if len(sys.argv)!=3:raise ValueError('usage: python compare_control.py cases.json note.txt')
        digest=hashlib.sha256(Path(sys.argv[2]).read_bytes()).hexdigest()
        rows=compare(json.loads(Path(sys.argv[1]).read_text('utf-8')),digest)
        print(json.dumps(dict(reference_sha256=digest,results=rows,actual_policy_test=False,external_actions=0),ensure_ascii=False,indent=2))
    except (ValueError,OSError,TypeError) as exc:print(str(exc),file=sys.stderr);sys.exit(2)
