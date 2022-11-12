# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:55:47 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 40 - Módulos, Classes e Objetos

"""

class MyStuff(object):
    
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES!")
        

thing = MyStuff()
thing.apple()
print(thing.tangerine)


class Song(object):
    
    def __init__(self, lyrics):
        self.lyrics = lyrics
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                       "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()