#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:13:32 2020

@author: carlosgodinho
"""

class CountFromBy:
    
    def __init__(self, v: int = 0, i: int = 1) -> None:
        self.val = v
        self.inc = i
        
    def increase(self) -> None:
        self.val += self.inc
        
    def __repr__(self) -> str:
        return str(self.val)
        
    

c1 = CountFromBy()
c1.increase()
print(c1)



c2 = CountFromBy(100, 10)
print(c2)
c2.increase()
print(c2)