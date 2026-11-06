"""Compare fictional redirect URLs and reported byte counts; not a causal or incident verdict."""
from urllib.parse import urlsplit,urljoin
from pathlib import Path
import json,argparse

def address(value):
    if not isinstance(value,str):raise ValueError('URL string required')
    p=urlsplit(value)
    if p.scheme not in ('http','https') or not p.hostname or p.username is not None or p.password is not None:raise ValueError('absolute training HTTP URL required')
    return value

def review(record):
    if not isinstance(record,dict):raise ValueError('object record required')
    original=address(record['request_url']);status=record['status']
    if type(status) is not int or status not in (200,302,307):raise ValueError('fixture status required')
    execution=record.get('endpoint_execution')
    if execution not in ('unknown','reported'):raise ValueError('endpoint execution evidence state required')
    if status in (302,307):
        if not isinstance(record.get('location'),str) or not record['location']:raise ValueError('location required')
        expected=address(urljoin(original,record['location']))
        next_url=record.get('next_request_url')
        if next_url is not None:address(next_url)
        facts=dict(kind='redirect',resolved_location=expected,next_request_record_present=next_url is not None,exact_url_match=next_url==expected,url_comparison_only=True)
    else:
        declared,observed=record['declared_body_bytes'],record['observed_body_bytes']
        if type(declared) is not int or type(observed) is not int or min(declared,observed)<0 or observed>declared:raise ValueError('bounded byte counts required')
        facts=dict(kind='body',declared_body_bytes=declared,observed_body_bytes=observed,body_complete_in_supplied_metadata=declared==observed,missing_bytes=declared-observed)
    return dict(id=record['id'],**facts,endpoint_execution=execution,real_evidence_verified=False,causality_verified=False,incident_verdict='unresolved',external_actions=0)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        d=json.loads(a.input.read_text(encoding='utf-8'))
        if d.get('schema')!='training-web-evidence-v1' or d.get('external_actions_allowed') is not False or not isinstance(d.get('records'),list) or not d['records']:raise ValueError('training contract required')
        print(json.dumps([review(r) for r in d['records']],indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError,AttributeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
