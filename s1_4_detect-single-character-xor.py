#! /usr/local/bin/python

# usage:
# $ s1_4_detect-single-character-xor 'path_to_encrypted_lines.txt'

import sys
import xor_single_character

x = xor_single_character

file_path = sys.argv[1]

print(x.guess_from_file(file_path))
