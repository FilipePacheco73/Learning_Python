# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:28:20 2022

@author: Z52XXR7

Livro: Aprendendo Python

Exercício 42 - É-um, Tem-um, Objetos e Classes

"""

# Animal é-um object (sim, é meio confuso), veja o crédito extra
class Animal(object):
    pass

## Dog é-um animal
class Dog(Animal):
    
    def __init__(self, name):
        ## ?? 
        self.name = name
        

## Cat é-um animal
class Cat(Animal):
    
    def __init__(self, name):
        ## Cat tem-um name
        self.name = name
        
## Person é-um objeto
class Person(object):
    
    def __init__(self, name):
        ## Person tem-um name
        self.name = name
    
        ## Person tem-um pet de algum tipo
        self.pet = None
    
## Employee é-um Person
class Employee(Person):
    
    def __init__(self, name,salary):
        ## ?? hmm, o que é essa mágica estranha?
        super(Employee, self).__init__(name)
        ## Employee tem-um salary
        self.salary = salary
        
## Fish é-um objeto
class Fish(object):
    pass

## Salmon é-um Fish
class Salmon(Fish):
    pass

## Halibut é-um Fish
class Halibut(Fish):
    pass

## rover é-um Dog
rover = Dog("Rover")

## satan é um Cat
satan = Cat("Satan")

## mary é um Person
mary = Person("Mary")

##
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()