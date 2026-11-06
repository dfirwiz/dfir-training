"""Compute JA3-style strings from fictional preselected fields, not packets or identities."""
import argparse,hashlib,json
from pathlib import Path
GREASE={0x0a0a+0x1010*i for i in range(16)}

def fingerprint(record):
    if not isinstance(record,dict) or type(record.get('legacy_version')) is not int or not 0<=record['legacy_version']<=65535:raise ValueError('legacy_version integer required')
    fields=[]
    for name in ('ciphers','extensions','groups','point_formats'):
        values=record.get(name)
        maximum=255 if name=='point_formats' else 65535
        if not isinstance(values,list) or any(type(v) is not int or not 0<=v<=maximum for v in values):raise ValueError('bounded integer arrays required')
        fields.append('-'.join(str(v) for v in values if name=='point_formats' or v not in GREASE))
    text=','.join([str(record['legacy_version']),*fields])
    return dict(id=record.get('id',''),ja3_style_string=text,md5=hashlib.md5(text.encode('ascii'),usedforsecurity=False).hexdigest(),packet_extraction_performed=False,negotiated_version_verified=False,identity_verified=False,incident_verdict='unresolved',external_actions=0)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);a=p.parse_args()
    try:
        data=json.loads(a.input.read_text(encoding='utf-8'))
        if data.get('schema')!='training-hello-fields-v1' or data.get('external_actions_allowed') is not False or not isinstance(data.get('records'),list) or not data['records']:raise ValueError('training contract required')
        print(json.dumps([fingerprint(r) for r in data['records']],indent=2));return 0
    except (OSError,ValueError,TypeError,AttributeError) as e:print('ERROR '+str(e));return 2
if __name__=='__main__':raise SystemExit(main())
