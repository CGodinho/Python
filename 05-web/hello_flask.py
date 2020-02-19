#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:35:07 2020

@author: carlosgodinho
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from Flask!'

@app.route('/echo')
def echo() -> str:
    return 'Echhho!'

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Echo tester')

app.run()   