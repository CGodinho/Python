# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 14:08:46 2020

@author: pt101492
"""


def add(val1, val2):
    return val1 + val2


def crazy_call(float_int: float, decimal_int: int = 10) -> str:
    summing = float_int + decimal_int
    return(str(summing))

print(add(1, 3))

# basic call
print(crazy_call(8.5, 2))

# name specified in attributes
print(crazy_call(float_int=4.1, decimal_int=3))

# no problem in changng order of attributes
print(crazy_call(decimal_int=3, float_int=4.1))

# decimal argument by default is set to 10
print(crazy_call(float_int=4.1))
