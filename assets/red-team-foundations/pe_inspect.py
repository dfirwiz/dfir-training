"""Read-only, deliberately small PE teaching inspector. Python 3.10+.

No execution, process access, writes, external packages, or network requests.
The --demo fixture is synthetic header data, not a runnable program.
This is not a complete PE validator or a malware verdict engine.
"""
import argparse
import json
from pathlib import Path
import struct


def demo_bytes():
    data = bytearray(1024)
    data[:2] = b'MZ'
    struct.pack_into('<i', data, 0x3c, 0x80)
    data[0x80:0x84] = b'PE\0\0'
    struct.pack_into('<HHIIIHH', data, 0x84, 0x8664, 1, 0, 0, 0, 0xf0, 0x22)
    opt = 0x98
    struct.pack_into('<H', data, opt, 0x20b)
    struct.pack_into('<I', data, opt + 16, 0)
    struct.pack_into('<Q', data, opt + 24, 0x140000000)
    struct.pack_into('<II', data, opt + 32, 0x1000, 0x200)
    struct.pack_into('<II', data, opt + 56, 0x2000, 0x200)
    struct.pack_into('<I', data, opt + 108, 16)
    data[0x188:0x190] = b'.data\0\0\0'
    struct.pack_into('<IIII', data, 0x190, 0x500, 0x1000, 0x200, 0x200)
    struct.pack_into('<I', data, 0x188 + 36, 0x40000040)
    data[0x320:0x32b] = b'LESSON-DEMO'
    return bytes(data)


def inspect(data, rva=None):
    def require(offset, size):
        if offset < 0 or size < 0 or offset + size > len(data):
            raise ValueError('truncated or out-of-bounds structure')

    def number(fmt, offset):
        require(offset, struct.calcsize(fmt))
        return struct.unpack_from(fmt, data, offset)[0]

    require(0, 64)
    if data[:2] != b'MZ':
        raise ValueError('missing MZ signature')
    pe = number('<i', 0x3c)
    if pe < 64:
        raise ValueError('invalid PE header offset')
    require(pe, 24)
    if data[pe:pe+4] != b'PE\0\0':
        raise ValueError('missing PE signature')
    coff = pe + 4
    machine = number('<H', coff)
    count = number('<H', coff + 2)
    opt_size = number('<H', coff + 16)
    if not 1 <= count <= 96:
        raise ValueError('section count outside this inspector scope')
    opt = coff + 20
    require(opt, opt_size)
    magic = number('<H', opt)
    minimum = {0x10b: 96, 0x20b: 112}.get(magic)
    if minimum is None or opt_size < minimum:
        raise ValueError('unsupported or truncated optional header')
    image_base = number('<Q' if magic == 0x20b else '<I', opt + (24 if magic == 0x20b else 28))
    result = {'file_size': len(data), 'pe_offset': hex(pe), 'machine': hex(machine),
              'format': 'PE32+' if magic == 0x20b else 'PE32',
              'preferred_image_base': hex(image_base),
              'entry_rva': hex(number('<I', opt + 16)), 'sections': []}
    table = opt + opt_size
    require(table, count * 40)
    for index in range(count):
        start = table + index * 40
        name = data[start:start+8].split(b'\0', 1)[0].decode('ascii', errors='replace')
        virtual_size, virtual_address, raw_size, raw_pointer = struct.unpack_from('<IIII', data, start + 8)
        if raw_size:
            require(raw_pointer, raw_size)
        result['sections'].append(dict(name=name, virtual_size=virtual_size,
                                       virtual_address=virtual_address,
                                       raw_size=raw_size, raw_pointer=raw_pointer))
    if rva is not None:
        if not 0 <= rva <= 0xffffffff:
            raise ValueError('RVA must fit an unsigned 32-bit value')
        result['query_rva'] = hex(rva)
        headers = number('<I', opt + 60)
        candidates = [s for s in result['sections']
                      if s['virtual_address'] <= rva < s['virtual_address'] + max(s['virtual_size'], s['raw_size'])]
        if rva < headers:
            require(rva, 1)
            result['location'] = dict(kind='headers', file_offset=hex(rva))
        elif len(candidates) > 1:
            raise ValueError('overlapping sections: ambiguous RVA')
        elif candidates:
            section = candidates[0]
            delta = rva - section['virtual_address']
            if delta < section['raw_size']:
                offset = section['raw_pointer'] + delta
                require(offset, 1)
                result['location'] = dict(kind='raw-backed', section=section['name'], file_offset=hex(offset))
            else:
                result['location'] = dict(kind='zero-filled', section=section['name'], file_offset=None)
        else:
            result['location'] = dict(kind='unmapped', file_offset=None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', nargs='?', type=Path)
    parser.add_argument('--demo', action='store_true')
    parser.add_argument('--rva', type=lambda value: int(value, 0))
    args = parser.parse_args()
    if args.demo == (args.path is not None):
        parser.error('choose exactly one: --demo or a local file path')
    try:
        data = demo_bytes() if args.demo else args.path.read_bytes()
        print(json.dumps(inspect(data, args.rva), indent=2))
    except (OSError, ValueError, struct.error) as error:
        parser.exit(1, f'inspection failed: {error}\n')


if __name__ == '__main__':
    main()
