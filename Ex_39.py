# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 09:09:39 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 39 - Dicionários, Ah, os Adoráveis Dicionários

"""

stuff = {'name':'Zed','age':39,'height':6*12+2}
print(stuff['name'])
print(stuff['age'])
print(stuff['height'])
stuff['city'] = "SF"
print(stuff['city'])

stuff[1] = "Wow"
stuff[2] = "Neato"
print(stuff[1])
print(stuff[2])

del stuff['city']
del stuff[1]
del stuff[2]
print(stuff)

# crie um mapeamento entre estados e siglas
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
    }

# crie um conjunto básico de estados e algumascidades deles
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
    }

# adicione mais algumas cidades
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# imprima algumas cidades
print('-'*10)
print('NY State has: ', cities['NY'])
print('OR State has: ', cities['OR'])

# imprima alguns estados
print('-'*10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# faça isso usando o dic state e depois cities
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
    
# agora faça ambos ao mesmo tempo
print('-'*10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")
    
print('-'*10)
# com segurança, obtenha uma sigla de um estado que pode não estar ali
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
    
# obtenha uma cidade com um valor padrão
city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is: {city}")