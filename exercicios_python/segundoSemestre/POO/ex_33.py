# -*- coding: utf-8 -*-
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Cachorro(Animal):
    def emitir_som(self):
        print('Cachorro está latindo \n')


class Gato(Animal):
    def emitir_som(self):
        print('Gato está miando \n')


class Cavalo(Animal):
    def emitir_som(self):
        print('Cavalo está relincho \n')


class Veterinario:
    def examinar(self, animal):
        animal.emitir_som()


dog = Cachorro("Rex", 3)
horse = Cavalo("Horse", 6)
cat = Gato("Tina", 1)

dog.emitir_som()          # exibe o som do cachorro
horse.emitir_som()        # exibe o som do cavalo
cat.emitir_som()          # exibe o som do gato

vet = Veterinario()
vet.examinar(dog)         # exibe o som do cachorro
vet.examinar(horse)       # exibe o som do cavalo
vet.examinar(cat)         # exibe o som do gato
