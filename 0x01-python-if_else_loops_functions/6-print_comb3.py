#!/usr/bin/python3
number_pairs = []
for x in range(0, 10):
    for y in range(x + 1, 10):
        number_pairs.append('{}{}'.format(x, y))
print(', '.join(number_pairs))
print('89')
