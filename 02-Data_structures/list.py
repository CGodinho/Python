# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 13:49:03 2020

"""

# creating mepty
numbers = []

# appending (to the end) of al ist
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(2)

# remove 1st occurence of an element
numbers.remove(2)

# reteives the last element and returns it
print('pop: ', numbers.pop())

# extending the list
numbers.extend([10, 20, 30, 40])

# inesrt onject at a position
numbers.insert(4, "something")

if (100 in numbers):
    print("100 is in list")
else:
    print("100 is not in list")

# Browsing over with a for and in operation
for number in numbers:
    print(number)
    
# stepping to create a reverse list
print(numbers[::-1])

# every odd position
print(numbers[::2])

# from 0 to 3 excluded
print(numbers[:3])

# from 3 to end
print(numbers[3:])

# party reversed
print(numbers[5:2:-1])