# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:08:52 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 15 - Lendo Arquivos


"""

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)
print(txt_again.read())

txt.close()
txt_again.close()