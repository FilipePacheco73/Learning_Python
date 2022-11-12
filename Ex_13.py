# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:38:39 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 13 - Parâmetros, Descompactação Variáveis

"""

from sys import argv

#leia a seção 0 que voce deve ver para saber como executar isso 

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)