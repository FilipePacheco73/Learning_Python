# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:49:22 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 8 - Imprimindo, imprimindo

"""

formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,False,True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))