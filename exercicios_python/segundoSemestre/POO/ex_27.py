# -*- coding: utf-8 -*-
class Animal():
    def __init__(self, nome, cor, num_patas):
        self.nome = nome
        self.cor = cor
        self.num_patas = num_patas

    def exibir_dados(self):
        print('Nome: {}'.format(self.nome))
        print('Cor: {}'.format(self.cor))
        print('Numero de patas: {}'.format(self.num_patas))


class Cachorro(Animal):
    def __init__(self, nome, cor, num_patas, raca):
        super().__init__(nome, cor, num_patas)
        self.raca = raca

    def exibir_dados(self):
        self.exibir_dados()
        print('Raça: {}'.format(self.raca))
