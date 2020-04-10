#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:04:28 2020

@author: carlosgodinho
"""


import pprint


def asDouble(value):
    return 2 * value


##############################################################################
#                     L I S T      C O M P R E H E N S I O N
##############################################################################
orig_list = [1, 2, 3, 4, 5, 6, 10, 20, 30, 100, 200]

print(orig_list)

# with basic structures
double_list = []
for value in orig_list:
    double_list.append(asDouble(value))
    
print(double_list)


# with comprehension
double_list2 = [asDouble(value) for value in orig_list]

print(double_list2)



##############################################################################
#              D I C T I O N A R Y      C O M P R E H E N S I O N
##############################################################################
orig_dict = {1 : 'one', 2 : 'two', 3 : 'three', 4: 'four'}

print(orig_dict)

# with basic structures
change_dict = {}

for k, v in orig_dict.items():
    change_dict[v] = k

print(change_dict)

# adding a filter condition
change_dict2 = {v : k for  k, v in orig_dict.items() if k < 3}

print(change_dict2)
pprint.pprint(change_dict2)

# may beocme complex
# res = {dest: [k for k, v in fts.items() if v == dest] for dest in set(fts.values())}


##############################################################################
#                   S E T     C O M P R E H E N S I O N
##############################################################################
vowels = {'a', 'e', 'i', 'o', 'u'}
message = 'is there any vowel?'

found_vowels = {vowel for vowel in message if vowel in vowels}

print(found_vowels)


##############################################################################
#                     G E N E R A T O R
# data is available as porcessed
# there are no comprehensions with tuples, as tuples are immutable
##############################################################################
for i in (2 * x for x in [1, 2, 3 ,4, 5]):
        print(i)