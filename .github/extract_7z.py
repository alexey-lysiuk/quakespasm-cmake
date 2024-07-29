#!/usr/bin/env python3

import sys

f = open(sys.argv[1], 'rb')
content = f.read()

header = b'7z\xbc\xaf\x27\x1c'
pos7z = content.find(header, content.find(header) + 1)
assert pos7z != 0

f = open('vulkan-sdk.7z', 'wb')
f.write(content[pos7z:])
