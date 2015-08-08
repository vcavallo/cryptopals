import string

numbers = ""
for n in range(0,9):
  numbers += str(n)
test_cases = string.ascii_lowercase + string.ascii_uppercase + numbers

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

def xor_string_by_one_character(string1, string2):
    string2 = string2 * len(string1)
    return "".join(chr(ord(zstring1) ^ ord(zstring2)) for zstring1, zstring2 in zip(string1, string2))

def guess_by_letter_frequency(collection):
  results = []

  for line in collection:
    test_results = {}
    test_results['string'] = line
    test_results['score'] = 0

    for letter, freq in standard_frequencies.iteritems():
      total = len(line)
      occur = line.count(letter)
      test_freq = (occur / float(total)) * 100
      test_results[letter] = round(test_freq, 2)
      test_results['score'] = test_results['score'] + abs(standard_frequencies[letter] - test_freq)

    results.append(test_results)

  winner = min(results, key=lambda x:x['score'])
  return winner['string']


def xor_against_all_chars(string):

  xored_lines = []
  for char in test_cases:
    xored = xor_string_by_one_character(string.strip().decode("hex"), char)
    xored_lines.append(xored)

  return guess_by_letter_frequency(xored_lines)

def guess_from_file(file_path):
  f = open(file_path, 'r')
  all_guesses = []
  for line in f:
    all_guesses.append(xor_against_all_chars(line))

  print(guess_by_letter_frequency(all_guesses))


