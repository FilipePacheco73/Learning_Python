# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 14:11:12 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 33 - Loops While

"""

i = 0

numbers = []

while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)
    
    i = i + 1
    print("Numbers now:", numbers)
    print(f"At the bottom i is {i}")
    
    print("The numbers: ")
    
    for num in numbers:
        print(num)