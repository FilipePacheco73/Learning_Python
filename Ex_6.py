# -*- coding: utf-8 -*-
"""
Created on Mon May  9 14:32:39 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 6 - Strings e Texto

"""

types_of_people = 10
x = f'There are {types_of_people} types of people.'

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f'I said: {x}')
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)