"""Read-only Zone.Identifier text review. No network, extraction, or execution.

Python 3.10+. --demo uses synthetic text held in memory; --zone-text reads an
already exported UTF-8 text file. This is not a Windows ADS collector or a
malware classifier. Missing metadata is reported as unknown, never safe.
"""
import argparse
import configparser
import hashlib
import json
from pathlib import Path
import re
import sys

MAX_BYTES = 65536
ZONES = {0: 'LocalMachine', 1: 'Intranet', 2: 'Trusted', 3: 'Internet', 4: 'Restricted'}


def review_zone(text):
    result = {'state': 'missing', 'zone_id': None, 'zone': None,
              'host_url_present': False, 'execution_proven': False,
              'maliciousness': 'undetermined'}
    if text is None:
        return result
    result['state'] = 'invalid'
    if len(text.encode('utf-8')) > MAX_BYTES:
        return result
    parser = configparser.ConfigParser(interpolation=None, strict=True)
    try:
        parser.read_string(text.lstrip('\ufeff'))
        if 'ZoneTransfer' not in parser:
            return result
        # Do not inherit a ZoneId from ConfigParser's DEFAULT section.
        own_fields = parser._sections['ZoneTransfer']
        raw = own_fields.get('zoneid', '').strip()
        if not re.fullmatch('[0-4]', raw):
            return result
        zone_id = int(raw)
        result.update(state='present', zone_id=zone_id, zone=ZONES[zone_id],
                      host_url_present=bool(own_fields.get('hosturl', '').strip()))
    except (configparser.Error, ValueError, TypeError):
        return result
    return result


def demo():
    body = b'TRAINING_ONLY\n'
    digest = hashlib.sha256(body).hexdigest()
    examples = [
        ('internet', '[ZoneTransfer]\nZoneId=3\nHostUrl=https://training.example/note.txt\n'),
        ('metadata-missing', None),
        ('invalid-zone', '[ZoneTransfer]\nZoneId=7\n'),
        ('intranet', '[ZoneTransfer]\nZoneId=1\n'),
    ]
    return {'synthetic': True, 'network_requests': 0, 'files_executed': 0,
            'cases': [dict(case=name, content_sha256=digest, **review_zone(text))
                      for name, text in examples]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument('--demo', action='store_true', help='review four synthetic cases')
    source.add_argument('--zone-text', type=Path, help='read existing exported UTF-8 text')
    args = parser.parse_args()
    try:
        if args.demo:
            result = demo()
        else:
            with args.zone_text.open('rb') as handle:
                data = handle.read(MAX_BYTES + 1)
            if len(data) > MAX_BYTES:
                raise ValueError('zone text exceeds 65536 bytes')
            result = review_zone(data.decode('utf-8-sig'))
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
