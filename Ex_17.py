# -*- coding: utf-8 -*-
"""
Created on Fri May 27 08:58:07 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 17 - Mais Arquivos

"""

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# poderíamos fazer esses dois com uma linha, como?
in_file = open(from_file)
indata = in_file.read()

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")
out_file.close()
in_file.close()