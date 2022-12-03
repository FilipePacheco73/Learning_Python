# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:04:23 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 51 - Obtendo Entrada de um Navegador

"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello")
def index():
    name = request.args.get('name','Nobody')
    greet = request.args.get('greet','Hello')

    if name:
        greeting = f"{greet}, {name}"
    else:
        greeting = "Hello World"
    
    return render_template("index.html",greeting=greeting)

if __name__ == "__main__":
    app.run()