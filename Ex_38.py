# -*- coding: utf-8 -*-
"""
Created on Wed Jul  6 15:34:48 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 38 - Fazendo Coisas com Listas

"""

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ['Day','Night','Song','Frisbee',
              'Corn','Banana','Girl','Boy']

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")
    
print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) # eita! que chique
print(stuff.pop())
print(' '.join(stuff)) # o quê? legal!
print('#'.join(stuff[3:5])) # show de bola !

