# -*- coding: utf-8 -*-


class Carro():
    def __init__(self, ma, mo, pla, an):
        self.marca = ma
        self.modelo = mo
        self.placa = pla
        self.ano = an


class Pessoa():
    def __init__(self, n, i):
        self.nome = n
        self.idade = i
        self.carr = None

    def comprar_carro(self, car):
        self.carr = car


meucarro = Carro('Volkswagen', 'Gol', 'AAA-1111', 2015)
eu = Pessoa('vinicius', 21)
eu.comprar_carro(meucarro)
print('Meu nome: ', eu.nome)
print('Modelo do meu carro: ', eu.carr.modelo)
print('Placa do meu carro: ', eu.carr.placa)
