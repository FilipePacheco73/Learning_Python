# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 13:25:50 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 51 - Obtendo Entrada de um Navegador

"""

from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/hello", methods=['POST','GET'])
def index():
    greeting = "Hello World"

    if request.method == "POST":
        name = request.form['name']
        greet = request.form['greet']
        greeting = f"{greet},{name}"
        return render_template("index.html",greeting=greeting)
    else:
        return render_template("hello_form.html")

if __name__ == "__main__":
    app.run()