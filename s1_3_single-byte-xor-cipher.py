#! /usr/local/bin/python

import sys
import string

given = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

# the function that XORs two strings
def xor_strings(string1, string2):
    # but actually we're expecting the second string to be a single character
    # and rather than figure out how that works here's a hack to use keep using zip
    string2 = string2 * len(string1)
    return "".join(chr(ord(zstring1) ^ ord(zstring2)) for zstring1, zstring2 in zip(string1, string2))


# since i don't know python well enough, here's another hack to get all the numbers
# for the purpose of adding to the ascii letter tables further down
numbers = ""
for n in range(0,9):
  numbers += str(n)

# set up all the character test cases
test_cases = string.ascii_lowercase + string.ascii_uppercase + numbers

# the letter frequency table needed to arrive at the most-likely english result
standard_frequencies = {
    'e': 12.49,
    't':  9.28,
    'a':  8.04,
    'o':  7.64,
    'i':  7.57,
    'n':  7.23,
    's':  6.51,
    'r':  6.28,
    'h':  5.05,
    'l':  4.07,
    'd':  3.82
}

results = []
# try XORing against each possible character
for char in test_cases:
    test_results = {}
    xored = xor_strings(given.decode("hex"), char)
    # add this string to the results
    test_results['string'] = xored

    test_results['score'] = 0

    # using the letter frequency table, give each string a score
    for letter, freq in standard_frequencies.iteritems():
      total = len(xored)
      occur = xored.count(letter)
      test_freq = (occur / float(total)) * 100

      # might as well throw all the raw data in there for testing
      test_results[letter] = round(test_freq, 2)

      # update the score with the difference from the table
      test_results['score'] = test_results['score'] + abs(standard_frequencies[letter] - test_freq)

    # add all the above computed crap to the results list
    results.append(test_results)

# only print out the lowest scored item (that is, closest to the normal frequency
# when totaling for all numbers. something like averages would probably be far better
print(min(results, key=lambda x:x['score']))
