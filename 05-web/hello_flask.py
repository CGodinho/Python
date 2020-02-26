#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 23:35:07 2020

@author: carlosgodinho
"""

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/results', methods=['POST'])
def echo() -> str:
    results = 'Echhho '+ request.form['message'] + '!!' 
    return render_template('results.html', the_title='Presenting results', the_results=results, the_message=request.form['message'],)

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Echo tester')

app.run(debug=True)   