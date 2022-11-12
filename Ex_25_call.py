# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:57:27 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 25 - Mais prática ainda

"""

import Ex_25

sentence = "All good things come to those who wait."
words = Ex_25.break_words(sentence)
words
sorted_words = Ex_25.sort_words(words)
sorted_words
Ex_25.print_first_word(words)
Ex_25.print_last_word(words)
words
Ex_25.print_first_word(sorted_words)
Ex_25.print_last_word(sorted_words)
sorted_words
sorted_words = Ex_25.sort_sentence(sentence)
sorted_words
Ex_25.print_first_and_last(sentence)
Ex_25.print_first_and_last_sorted(sentence)