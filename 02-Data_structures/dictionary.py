# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 09:54:14 2020

"""

empty_dict = {}

person = { 'Name' : 'Joselito',
           'Gender' : 'Male',
           'Occupation' : 'Carraça',
           'Home' : 'Lixeira'}


# insert order hsad no meaning
print(person)

# accessing a member
print(person['Name'])

# Key error exception when searching for a wrong key
# print(person['Not found'])

# Adding a new <key, value>
person['Age'] = 99
print(person)

# Joselito is becoming centenary
person['Age'] += 1
print(person)

# browsing over
for key in person:
    print(key, 'is', person[key])

# more advance browsing
for key, value in person.items():
    print(key, 'is', value)

# set a default value before assigment ot avoid Key Error
person.setdefault('Weight', 0)
person['Weight'] = 120
print(person)

# check if a key isa in dict
print('Weight' in person)