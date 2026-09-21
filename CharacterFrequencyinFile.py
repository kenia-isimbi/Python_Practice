import collections  # Import the 'collections' module for Counter.
import pprint  # Import 'pprint' for pretty printing.

file_input = input('File Name: ')

with open(file_input, 'r') as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)

print(value)
