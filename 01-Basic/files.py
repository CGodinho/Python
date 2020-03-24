# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:54:54 2020

@author: CGodinho
"""

# Write to a new file using basic API
data_file = open('example.txt', 'w')
print('Hello!', file=data_file)
print('This is an example', file=data_file)
print('On writing to a text file!', file=data_file)
data_file.close()
    

# Reading from file using 'with'
# Content management protocol applied woth dunders enter and exit
with open('example.txt', 'r') as data_file:
    for line in data_file:
        print('Line : ', line)