# -*- coding: utf-8 -*-
"""
Created on Tue May 10 15:58:16 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 14 - Prompt e Passagem

"""

from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
