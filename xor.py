import sys

def xor_strings(string1, string2):
    return "".join(chr(ord(zstring1) ^ ord(zstring2)) for zstring1, zstring2 in zip(string1, string2))

binary_a = sys.argv[1].decode("hex")
binary_b = sys.argv[2].decode("hex")

xored = xor_strings(binary_a, binary_b)

print(xored.encode("hex"))
