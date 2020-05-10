# -*- coding: utf-8 -*-
class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.salario_base = salario_base

    def calcular_salario(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        print(self.salario_base * 2)


class Assistente(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        print(self.salario_base)


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_base):
        super().__init__(nome, matricula, salario_base)

    def calcular_salario(self):
        self.salario_base += self.salario_base * 0.10
        print(self.salario_base)


func = []

ger = Gerente('vinicius', 10, 1000)
assis = Assistente('Cecília', 11, 1000)
vend = Vendedor('Thayna', 12, 1000)

func.append(ger)
func.append(assis)
func.append(vend)

for f in func:
    f.calcular_salario()
