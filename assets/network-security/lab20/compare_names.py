"""Compare fictional source records. Does not resolve real-world actor identity or fetch reports."""
import argparse
from datetime import date
import json
from pathlib import Path


def compare(data, label='Training Birch', record_id=None):
    if not isinstance(data, dict) or data.get('schema') != 'training-names-v1':
        raise ValueError('training-names-v1 object required')
    rows = data['records']
    if not isinstance(rows, list) or not rows or not isinstance(data['relations'], list):
        raise ValueError('records and relations lists required')
    records = {}
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError('record must be an object')
        for key in ('record_id','publisher','tracking_id','label','entity_type','as_of','report'):
            if not isinstance(row.get(key), str) or not row[key]:
                raise ValueError('non-empty record fields required')
        if row['record_id'] in records:
            raise ValueError('duplicate record id')
        date.fromisoformat(row['as_of'])
        if not row['report'].startswith('https://reports.example/'):
            raise ValueError('fictional report URL required')
        records[row['record_id']] = row
    relations = data['relations']
    for rel in relations:
        if not isinstance(rel, dict) or rel['from'] not in records or rel['to'] not in records:
            raise ValueError('relation references an unknown record')
        if rel['kind'] not in ('same_source_rename','reported_overlap') or not rel.get('basis'):
            raise ValueError('relation kind and basis required')
        if rel['kind'] == 'same_source_rename':
            a, b = records[rel['from']], records[rel['to']]
            if any(a[k] != b[k] for k in ('publisher','tracking_id','entity_type')):
                raise ValueError('rename must preserve source identity and entity type')
    matches = [r for r in rows if r['record_id'] == record_id] if record_id else [r for r in rows if r['label'] == label]
    if not matches:
        return dict(status='no_record_in_this_dataset',real_actor_verdict='unresolved')
    if len(matches) != 1:
        return dict(status='ambiguous_label',matches=[r['record_id'] for r in matches],automatic_merge=False)
    anchor = matches[0]['record_id']
    same = {anchor}
    changed = True
    while changed:
        changed = False
        for rel in relations:
            if rel['kind'] == 'same_source_rename' and (rel['from'] in same or rel['to'] in same):
                old = len(same);same.update((rel['from'],rel['to']));changed |= len(same) != old
    overlap = set()
    for rel in relations:
        if rel['kind'] != 'reported_overlap':
            continue
        if rel['from'] in same and rel['to'] not in same:
            overlap.add(rel['to'])
        if rel['to'] in same and rel['from'] not in same:
            overlap.add(rel['from'])
    labels = {records[i]['label'] for i in same | overlap}
    collisions = {r['record_id'] for r in rows if r['record_id'] not in same | overlap and r['label'] in labels}
    return dict(status='source_record_comparison_only',anchor=anchor,
                same_source_identity=sorted(same),direct_overlap_candidates=sorted(overlap),
                same_label_other_records=sorted(collisions),
                overlap_is_transitive=False,real_actor_verdict='unresolved',external_lookups=0)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('file',type=Path)
    p.add_argument('--label',default='Training Birch')
    p.add_argument('--record-id',help='Select one record instead of matching a label')
    args = p.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding='utf-8'))
        print(json.dumps(compare(data,args.label,args.record_id),ensure_ascii=False,indent=2))
        return 0
    except (OSError,ValueError,TypeError,KeyError,AttributeError) as exc:
        print('ERROR '+str(exc))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
