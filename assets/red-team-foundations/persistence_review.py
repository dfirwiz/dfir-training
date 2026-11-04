#!/usr/bin/env python3
"""Read small, local task XML texts. Never register a task or execute its action.
Python 3.10+, standard library. Output describes XML, not runtime truth/XSD validation.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path
import xml.etree.ElementTree as ET

NS = 'http://schemas.microsoft.com/windows/2004/02/mit/task'
LIMIT = 65536
PREFIX = '{' + NS + '}'


def inspect_xml(raw):
    if len(raw) > LIMIT:
        raise ValueError('XML exceeds 65536 bytes')
    text = raw.decode('utf-8-sig')
    if '<!DOCTYPE' in text.upper() or '<!ENTITY' in text.upper():
        raise ValueError('DTD/entity declarations are not accepted')
    root = ET.fromstring(text)
    if root.tag != PREFIX + 'Task':
        raise ValueError('Expected Task with the official Task Scheduler namespace')

    def get(node, path):
        found = node.find('/'.join(PREFIX + p for p in path.split('/')))
        return None if found is None else (found.text or '').strip()

    def boolean(value, default):
        if value is None:
            return {'value': default, 'source': 'schema default; element absent'}
        if value not in ('true', 'false', '1', '0'):
            raise ValueError('Invalid XML boolean: ' + repr(value))
        return {'value': value in ('true', '1'), 'source': 'explicit XML'}

    triggers = root.find(PREFIX + 'Triggers')
    actions = root.find(PREFIX + 'Actions')
    principals = root.find(PREFIX + 'Principals')
    ts = []
    for t in ([] if triggers is None else triggers):
        if not t.tag.startswith(PREFIX):
            raise ValueError('Unexpected trigger namespace')
        ts.append({'type': t.tag[len(PREFIX):], 'user_id': get(t, 'UserId'),
                   'start_boundary': get(t, 'StartBoundary'),
                   'enabled': boolean(get(t, 'Enabled'), True)})
    ac = []
    for a in ([] if actions is None else actions):
        if not a.tag.startswith(PREFIX):
            raise ValueError('Unexpected action namespace')
        kind = a.tag[len(PREFIX):]
        ac.append({'type': kind, 'command': get(a, 'Command') if kind == 'Exec' else None,
                   'arguments': get(a, 'Arguments') if kind == 'Exec' else None,
                   'working_directory': get(a, 'WorkingDirectory') if kind == 'Exec' else None,
                   'class_id': get(a, 'ClassId') if kind == 'ComHandler' else None})
    ps = []
    for p in ([] if principals is None else principals):
        ps.append({'user_id': get(p, 'UserId'), 'group_id': get(p, 'GroupId'),
                   'logon_type': get(p, 'LogonType'), 'run_level': get(p, 'RunLevel')})
    enabled = boolean(get(root, 'Settings/Enabled'), True)
    warnings = []
    if not enabled['value']:
        warnings.append('Task is disabled in this definition; runtime not checked')
    if not ts:
        warnings.append('No triggers in XML; not proof that a manual run is impossible')
    if not ac:
        warnings.append('No actions in XML; definition may be incomplete')
    if any(a['type'] != 'Exec' for a in ac):
        warnings.append('Non-Exec action preserved; no activation or execution attempted')
    return {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
            'definition_enabled': enabled, 'principals': ps, 'triggers': ts,
            'actions': ac, 'warnings': warnings,
            'limits': 'Static extraction only; no XSD validation, registration, execution, or maliciousness verdict'}


def demo_cases():
    base = '''<Task xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
<Triggers><LogonTrigger><UserId>LAB-PC\\student</UserId><Enabled>true</Enabled></LogonTrigger></Triggers>
<Principals><Principal><UserId>LAB-PC\\student</UserId><LogonType>InteractiveToken</LogonType><RunLevel>LeastPrivilege</RunLevel></Principal></Principals>
<Settings><Enabled>true</Enabled></Settings>
<Actions><Exec><Command>C:\\Windows\\System32\\notepad.exe</Command></Exec></Actions></Task>'''
    return [('enabled-logon', base.encode()),
            ('disabled-task', base.replace('<Settings><Enabled>true', '<Settings><Enabled>false').encode()),
            ('no-triggers', base.replace('<Triggers><LogonTrigger><UserId>LAB-PC\\student</UserId><Enabled>true</Enabled></LogonTrigger></Triggers>', '<Triggers/>').encode()),
            ('wrong-namespace', base.replace(NS, 'urn:training:wrong').encode())]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument('--demo', action='store_true')
    group.add_argument('--xml', type=Path, help='Existing UTF-8 XML file, <=64 KiB')
    args = ap.parse_args()
    if args.demo:
        for name, raw in demo_cases():
            try:
                result = inspect_xml(raw)
            except (ValueError, ET.ParseError, UnicodeError) as exc:
                result = {'error': str(exc)}
            print(json.dumps({'case': name, **result}, ensure_ascii=False))
        return 0
    try:
        with args.xml.open('rb') as stream:
            raw = stream.read(LIMIT + 1)
        print(json.dumps(inspect_xml(raw), ensure_ascii=False, indent=2))
    except (OSError, ValueError, ET.ParseError, UnicodeError) as exc:
        print(json.dumps({'error': str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
