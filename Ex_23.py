# -*- coding: utf-8 -*-
"""
Created on Fri May 27 14:35:51 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 23 - Strings, Bytes e Codificações de Caracteres

"""

import sys

script, enconding, error = sys.argv

def main(language_file, enconding, errors):
    line = language_file.readline()
    
    if line:
        print_line(line, enconding, errors)
        return main(language_file, enconding, errors)
    
def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    
    print(raw_bytes, "<===>", cooked_string)
    
languages = open('Ex_23_sample.txt', encoding='utf-8')

main(languages, enconding, error)