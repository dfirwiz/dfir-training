"""Offline learning exercise. Not a MISP client, schema validator or publisher."""
import argparse
import json
from pathlib import Path
import re
from collections import defaultdict
from datetime import date


def validate(data):
    if not isinstance(data, dict) or data.get('schema') != 'training-cti-v1':
        raise ValueError('expected training-cti-v1 object')
    events = data.get('events')
    if not isinstance(events, list) or not events:
        raise ValueError('events must be a non-empty list')
    issues = []
    ids = set()
    for event in events:
        if not isinstance(event, dict):
            raise ValueError('event must be an object')
        eid = event['id']
        if not isinstance(eid, str) or not eid or eid in ids:
            raise ValueError('duplicate or invalid event id')
        ids.add(eid)
        date.fromisoformat(event['date'])
        if not isinstance(event.get('attributes'), list) or not event['attributes']:
            raise ValueError('attributes must be a non-empty list')
        if event.get('review_state') != 'reviewed':
            issues.append(eid + ': event review pending')
        if not isinstance(event.get('source'), str) or not event['source'].startswith('https://reports.example/'):
            issues.append(eid + ': training source missing')
        if event.get('distribution') != 'organisation-only' or event.get('tlp') != 'TLP:AMBER+STRICT':
            issues.append(eid + ': exercise sharing scope changed')
        aids = set()
        for a in event['attributes']:
            aid = a['id']
            if not isinstance(aid, str) or not aid or aid in aids:
                raise ValueError('duplicate or invalid attribute id')
            aids.add(aid)
            label = eid + '/' + aid
            typ, value = a['type'], a['value']
            if typ not in ('sha256', 'domain', 'link') or not isinstance(value, str) or not value:
                raise ValueError('unsupported type or empty value')
            if type(a.get('to_ids')) is not bool or type(a.get('seen_locally')) is not bool:
                raise ValueError('to_ids and seen_locally must be JSON booleans')
            if typ == 'sha256' and not re.fullmatch(r'[0-9a-f]{64}', value):
                issues.append(label + ': invalid sha256 shape')
            if typ == 'domain' and value != 'files.example':
                issues.append(label + ': unexpected training domain')
            if a.get('review_state') != 'reviewed' or not a.get('comment'):
                issues.append(label + ': attribute review pending')
            expected = {'sha256': ('Payload delivery', 'file-candidate'),
                        'domain': ('Network activity', 'role-unconfirmed'),
                        'link': ('External analysis', 'reference')}[typ]
            if (a.get('category'), a.get('role')) != expected:
                issues.append(label + ': category or role needs review')
            if typ == 'link' and (a['to_ids'] or not value.startswith('https://reports.example/')):
                issues.append(label + ': reference must not be detection candidate')
            if a['to_ids'] and a.get('role') != 'file-candidate':
                issues.append(label + ': detection use not justified in this exercise')
    return issues


def run(data, mode):
    issues = validate(data)
    if issues:
        for issue in issues:
            print('REVIEW ' + issue)
        return 2
    print('CHECK reviewed-shape-only; truth and permission not verified')
    if mode == 'correlate':
        groups = defaultdict(set)
        for e in data['events']:
            for a in e['attributes']:
                if a['type'] == 'sha256':
                    groups[(a['type'], a['value'])].add(e['id'])
        for (typ, value), events in sorted(groups.items()):
            if len(events) > 1:
                print(f'CORRELATION {typ}:{value} events={",".join(sorted(events))}; attribution=unknown')
    if mode == 'plan':
        candidates = {(a['type'], a['value']) for e in data['events']
                      for a in e['attributes'] if a['to_ids']}
        for typ, value in sorted(candidates):
            print(f'LOCAL-PLAN {typ}:{value}')
        print(f'PLAN unique-candidates={len(candidates)}; external-transfer=NOT-PERFORMED')
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['check', 'correlate', 'plan'])
    parser.add_argument('record', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.record.read_text(encoding='utf-8'))
        return run(data, args.mode)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print('ERROR ' + str(exc))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
