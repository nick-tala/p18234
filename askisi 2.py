import collections
import pprint
file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())

for x, y in count.items():
    a_string = "#" * y
    print(x, y, '\t', a_string)
