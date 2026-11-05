"""Offline replay of fictional lookup outcomes. Plans only; no API, network or case writes."""
import argparse
import json
from pathlib import Path


def replay(data, max_attempts=2):
    if not isinstance(data, dict) or data.get('schema') != 'training-workflow-v1':
        raise ValueError('training-workflow-v1 object required')
    if type(max_attempts) is not int or not 1 <= max_attempts <= 3:
        raise ValueError('max_attempts must be 1..3 per delivery')
    if data.get('external_transfer_allowed') is not False:
        raise ValueError('this exercise permits no external transfer')
    version = data['workflow_version']
    tenant = data['tenant']
    records = data['deliveries']
    if not all(isinstance(x, str) and x for x in (version, tenant)) or not isinstance(records, list) or not records:
        raise ValueError('version/tenant/non-empty deliveries required')
    completed = set()
    contexts = {}
    pending = {}
    notes = []
    audit = []
    attempts = duplicates = 0
    for rec in records:
        if not isinstance(rec, dict):
            raise ValueError('delivery must be an object')
        did, eid, case = rec['delivery_id'], rec['event_id'], rec['case_id']
        value = rec['observable']['value']
        if not all(isinstance(x, str) and x for x in (did, eid, case, value)):
            raise ValueError('non-empty string identifiers required')
        if rec['observable']['type'] != 'domain' or not value.endswith('.example'):
            raise ValueError('only fictional .example domains in this exercise')
        key = (tenant, case, eid, version)
        context = ('domain', value)
        if key in contexts and contexts[key] != context:
            raise ValueError('same planning key has conflicting context')
        contexts[key] = context
        results = rec['mock_lookup_results']
        if not isinstance(results, list) or not results:
            raise ValueError('non-empty mock outcomes required')
        for result in results:
            if not isinstance(result, dict) or result.get('status') not in ('timeout','ok','permission_denied'):
                raise ValueError('invalid mock status')
            if result['status'] == 'ok' and result.get('verdict') not in ('suspicious','no_match'):
                raise ValueError('invalid mock verdict')
        if key in completed:
            duplicates += 1
            audit.append(dict(delivery=did,state='duplicate_plan_skipped'))
            continue
        final = 'retry_budget_exhausted'
        for number, result in enumerate(results[:max_attempts], 1):
            attempts += 1
            status = result['status']
            audit.append(dict(delivery=did,attempt=number,status=status,simulation=True))
            if status == 'timeout':
                continue
            if status == 'permission_denied':
                final = 'permission_review_required'
                break
            verdict = result.get('verdict')
            notes.append(dict(planning_key=list(key),observable=value,
                              lookup_claim=verdict,decision='human_review_required',
                              action='local_note_plan_only'))
            completed.add(key)
            pending.pop(key, None)
            final = 'planned'
            break
        if final != 'planned':
            pending[key] = final
    return dict(mode='offline-replay; no external effects',deliveries=len(records),
                simulated_lookup_attempts=attempts,duplicate_plans_skipped=duplicates,
                note_plans=notes,pending=[dict(planning_key=list(k),reason=v) for k,v in sorted(pending.items())],
                audit=audit,external_requests=0,case_writes=0,blocks=0)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('file',type=Path)
    p.add_argument('--max-attempts',type=int,default=2)
    args = p.parse_args()
    try:
        data = json.loads(args.file.read_text(encoding='utf-8'))
        print(json.dumps(replay(data,args.max_attempts),ensure_ascii=False,indent=2))
        return 0
    except (OSError,ValueError,KeyError,TypeError,AttributeError) as exc:
        print('ERROR '+str(exc))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
