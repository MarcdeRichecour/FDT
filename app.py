#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:50:06 2020

@author: marcd
"""

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
   return render_template('example.html')
if __name__ == '__main__':
   app.run()
   
   
   
   
   
   
   
   
   
   
   