# -*- coding: utf-8 -*-

# an empty set
numbers = set()
print(type(numbers))

# no duplication
numbers.add(1)
numbers.add(1)
numbers.add(2)
numbers.add(3)
numbers.add(4)
numbers.add(2)
print(numbers)


set1 = {'a', 'b', 'x', 'y'}
set2 = {'a', 'c', 'x', 'z'}

# set operators
print('union', set1.union(set2))
print('intersection', set1.intersection(set2))
print('difference', set1.difference(set2))
print('simmetric difference', set1 ^ set2)

# remove an element
numbers.remove(1)
print(numbers)

# check presence
print(3 in numbers)

# check # element
print(len(numbers))

# convert to a list
print(list(numbers))