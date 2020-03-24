#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:35:33 2020

@author: carlosgodinho
"""


try:
    with open('afile.txt') as fh:    
        data = fh.read()
    print(data)
except FileNotFoundError:
    print("File not available!")
except PermissionError:
    print("No permissions to file")
except Exception as err:
    print('Some other exception occurred:', str(err))