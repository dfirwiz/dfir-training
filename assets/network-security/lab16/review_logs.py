"""Offline fixed-window teaching example. Not KQL, an Elastic rule, or an attack verdict."""
import argparse
from collections import defaultdict
from datetime import datetime, timezone
import json
from pathlib import Path


def instant(value):
    if not isinstance(value, str):
        raise ValueError('timestamp must be a string')
    dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    if dt.tzinfo is None:
        raise ValueError('timestamp must include UTC offset')
    return dt.astimezone(timezone.utc)


def analyse(rows, start, end, available_by, time_field, threshold):
    if not rows or start >= end or threshold < 1:
        raise ValueError('non-empty rows, start < end and positive threshold required')
    available = scoped = duplicates = missing_identity = 0
    seen = {}
    groups = defaultdict(list)
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('each line must be a JSON object')
        event = row['event']
        event_time = instant(row['@timestamp'])
        ingest_time = instant(event['ingested'])
        if ingest_time > available_by:
            continue
        available += 1
        chosen = event_time if time_field == 'event' else ingest_time
        if not start <= chosen < end:
            continue
        scoped += 1
        host, dataset, eid = row['host']['name'], event['dataset'], event['id']
        if not all(isinstance(x, str) and x for x in (host, dataset, eid)):
            raise ValueError('host/dataset/event id required')
        key = (dataset, host, eid)
        stable = {k: v for k, v in row.items() if k != '_record_id'}
        stable['event'] = {k: v for k, v in event.items() if k != 'ingested'}
        fingerprint = json.dumps(stable, sort_keys=True)
        if key in seen:
            if seen[key] != fingerprint:
                raise ValueError('same assumed event identity has conflicting content')
            duplicates += 1
            continue
        seen[key] = fingerprint
        category = event['category']
        if not isinstance(category, list):
            raise ValueError('event.category must be a list in this exercise')
        if 'authentication' not in category or event['outcome'] != 'failure':
            continue
        user = row.get('user', {})
        identity = (user.get('domain'), user.get('name'), row.get('source', {}).get('ip'))
        if not all(isinstance(v, str) and v for v in identity):
            missing_identity += 1
            continue
        groups[(host, *identity)].append(eid)
    candidates = []
    for (host, domain, user, source), ids in sorted(groups.items()):
        if len(ids) >= threshold:
            candidates.append(dict(host=host,domain=domain,user=user,source=source,count=len(ids),event_ids=ids))
    return dict(status='toy-condition-only; not KQL or compromise verdict',
                rows_total=len(rows),rows_available=available,time_in_scope=scoped,
                duplicates=duplicates,missing_identity=missing_identity,
                selected=sum(len(v) for v in groups.values()),groups=len(groups),
                time_field=time_field,threshold=threshold,candidates=candidates)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('file', type=Path)
    p.add_argument('--start', default='2026-11-05T09:00:00Z')
    p.add_argument('--end', default='2026-11-05T09:05:00Z')
    p.add_argument('--available-by', default='2026-11-05T09:15:00Z')
    p.add_argument('--time-field', choices=['event', 'ingest'], default='event')
    p.add_argument('--threshold', type=int, default=3)
    args = p.parse_args()
    try:
        rows = [json.loads(s) for s in args.file.read_text(encoding='utf-8').splitlines() if s.strip()]
        result = analyse(rows, instant(args.start), instant(args.end), instant(args.available_by), args.time_field, args.threshold)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        print('ERROR ' + str(exc))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
