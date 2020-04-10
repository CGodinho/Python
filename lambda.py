#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 16:34:26 2020

@author: carlosgodinho
"""

x = lambda a : 2 * a
print(x(4))


# Instantiate multiple vsriatinos of a function
def myfunc(n):
    return lambda a : n * a    
    
mydouble = myfunc(2)
mytriple = myfunc(3)

print(mydouble(5))
print(mytriple(5))    