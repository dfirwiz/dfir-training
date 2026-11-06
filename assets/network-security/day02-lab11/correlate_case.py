"""Compare a course HTTP fixture with separate fictional reports; no incident verdict."""
import argparse,json,re,hashlib,ipaddress
from pathlib import Path
from datetime import datetime,timezone

def utc(value):
    if not isinstance(value,str):raise ValueError('timestamp string required')
    t=datetime.fromisoformat(value)
    if t.tzinfo is None:raise ValueError('timezone required')
    return t.astimezone(timezone.utc)

def correlate(case,capture):
    if not isinstance(case,dict) or case.get('schema')!='training-web-correlation-v1' or case.get('external_actions_allowed') is not False:raise ValueError('training contract required')
    reports=case.get('endpoint_reports')
    if not isinstance(reports,list) or not reports:raise ValueError('fictional endpoint reports required')
    reference=utc(case['analyst_reference_time']);rows=[]
    for row in reports:
        if not isinstance(row,dict) or not isinstance(row.get('id'),str) or not row['id'] or not isinstance(row.get('reported_file_sha256'),str) or not re.fullmatch('[0-9a-f]{64}',row['reported_file_sha256']):raise ValueError('report ID and lower-case SHA256 required')
        if row.get('execution') not in ('unknown','reported'):raise ValueError('execution claim state required')
        t=utc(row['time'])
        rows.append(dict(id=row['id'],reported_time_utc=t.isoformat(),seconds_after_fictional_reference=(t-reference).total_seconds(),reported_execution=row['execution'],reported_file_sha256=row['reported_file_sha256'],endpoint_report_verified=False,same_transfer_verified=False,execution_verified=False))
    tls=case['tls_observation']
    if not isinstance(tls,dict) or type(tls.get('port')) is not int or not 1<=tls['port']<=65535:raise ValueError('TLS summary object and valid port required')
    for key in ('client','server'):ipaddress.ip_address(tls[key])
    for key in ('http_path','http_body','process_identity'):
        if key not in tls or (tls[key] is not None and not isinstance(tls[key],str)):raise ValueError('explicit unknown/string summary fields required')
    # Download inspect_http.py from the earlier course lab into this directory.
    from inspect_http import inspect
    import dpkt
    try:http=inspect(capture)
    except dpkt.Error as e:raise ValueError('unsupported or damaged fixture packet: '+str(e)) from e
    bodyhash=http.get('decoded_sha256')
    for row in rows:row['reported_hash_matches_observed_body']=row['reported_file_sha256']==bodyhash if bodyhash is not None else None
    return dict(capture_sha256=hashlib.sha256(Path(capture).read_bytes()).hexdigest(),http_fixture=http,endpoint_comparisons=rows,tls_supplied_summary=tls,tls_summary_verified=False,tls_packets_analyzed=False,packet_timestamp_correlation_performed=False,incident_verdict='unresolved',external_actions=0)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('case',type=Path);p.add_argument('capture',type=Path);a=p.parse_args()
    try:
        print(json.dumps(correlate(json.loads(a.case.read_text(encoding='utf-8')),a.capture),indent=2));return 0
    except (OSError,ValueError,TypeError,KeyError,ImportError,EOFError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
