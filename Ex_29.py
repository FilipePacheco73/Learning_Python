# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:52:06 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 29 - A instrução If

"""

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")
    
if people > cats:
    print("Not many cats! The world is saved!")
    
if people < dogs:
    print("The world is drooled on!")
    
if people > dogs:
    print("The world is dry!")
    
dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")
    
if people <= dogs:
    print("People are less than or equal to dogs.")
    
if people == dogs:
    print("People are dogs.")