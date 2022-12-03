# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 07:49:16 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 50 - Seu Primeiro Website

"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()
