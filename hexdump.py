#! /usr/bin/python

import sys
import base64

if len(sys.argv) > 1:
    options = sys.argv[1]
else:
    options = 'not given'

for line in sys.stdin:
    # need to strip to remove newline at end
    # which results in odd-length string error
    hex_decoded = line.strip().decode('hex')
    base64_encoded = base64.b64encode(hex_decoded)

    if options == '-h':
        output = hex_decoded
    elif options == '-h64':
        output = base64_encoded
    else:
        output = "please pass -h or -h64 args"

    sys.stdout.write(output)
