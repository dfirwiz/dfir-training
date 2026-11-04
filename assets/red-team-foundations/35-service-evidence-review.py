"""Classify supplied synthetic facts; never inspect or modify system ACLs."""
import json
from pathlib import Path
import sys

FIELDS = ('file_change', 'key_set_value', 'higher_context', 'input_linked')


def classify(case):
    if not isinstance(case, dict):
        raise ValueError('case must be an object')
    if not isinstance(case.get('id'), str) or not case['id']:
        raise ValueError('id must be a nonempty string')
    for field in FIELDS:
        if field not in case or (case[field] is not None and type(case[field]) is not bool):
            raise ValueError(f'{field} must be true, false, or null')
    if case['higher_context'] is False:
        return '높은 문맥 상승 미지지'
    changes = (case['file_change'], case['key_set_value'])
    if all(value is False for value in changes):
        return '변경 가설 미지지'
    if case['input_linked'] is False:
        return '실행 연결 미지지'
    if (any(value is True for value in changes)
            and case['higher_context'] is True and case['input_linked'] is True):
        return '조건부 위험 — 반영·실행 미검증'
    return '추가 확인 필요'


def review(data):
    if not isinstance(data, list) or not data:
        raise ValueError('expected nonempty list of synthetic facts')
    ids = set()
    lines = []
    for case in data:
        result = classify(case)
        if case['id'] in ids:
            raise ValueError('duplicate id')
        ids.add(case['id'])
        lines.append(f"{case['id']}: {result}")
    return lines


if __name__ == '__main__':
    try:
        if len(sys.argv) != 2:
            raise ValueError('usage: python3 35-service-evidence-review.py cases.json')
        data = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
        print('\n'.join(review(data)))
    except (OSError, ValueError) as error:
        print(f'input error: {error}', file=sys.stderr)
        sys.exit(2)
