# -*- coding: utf-8 -*-
"""
Created on Fri May 27 13:11:12 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 21 - As funções podem retornar algo

"""

def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a,b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a,b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a,b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# Uma charada para ponto extra, digite isso.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight,divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")