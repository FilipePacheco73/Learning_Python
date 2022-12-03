# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 08:30:48 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 50 - Seu Primeiro Website

"""

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World"
    return render_template("index.html")#greeting)

if __name__ == "__main__":
    app.run()
