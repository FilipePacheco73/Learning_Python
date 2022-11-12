# -*- coding: utf-8 -*-
"""
Created on Fri May 27 09:42:28 2022

@author: Filipe Pacheco

Livro: Aprendendo Python

Exercício 20 - Funções e Arquivos

"""

from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)

print("First let's print the while file:\n")

print_all(current_file)

print("Let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)