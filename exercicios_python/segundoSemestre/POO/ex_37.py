# -*- coding: utf-8 -*-
class Conta:
    def __init__(self, num_conta, nome, saldo):
        self.num_conta = num_conta
        self.nome = nome
        self.saldo = saldo

    def depositar(self, valor):
        pass

    def sacar(self, valor):
        pass

    def imprimir(self):
        pass


class ContaComum(Conta):
    def __init__(self, num_conta, nome, saldo, ):
        super().__init__(num_conta, nome, saldo)

    def depositar(self, valor):
        self.saldo += valor
        print('Valor depositado com sucesso!!!\n')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print('Saque realizado com sucesso!!!\n')
        else:
            print('Saldo insuficiente\n')

    def imprimir(self):
        print('Saldo atual:{}\n'.format(self.saldo))


class ContaPoupanca(Conta):
    def __init__(self, num_conta, nome, saldo, aniver_conta):
        super().__init__(num_conta, nome, saldo)
        self.aniver_conta = aniver_conta

    def depositar(self, valor):
        self.saldo += valor
        print('Valor depositado com sucesso!!!\n')

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print('Saque realizado com sucesso!!!\n')
        else:
            print('Saldo insuficiente\n')

    def imprimir(self):
        print('Saldo atual:{}\n'.format(self.saldo))


class ContaLimite(Conta):
    def __init__(self, num_conta, nome, saldo, valor_limite):
        super().__init__(num_conta, nome, saldo)
        self.valor_limite = -valor_limite

    def depositar(self, valor):
        self.saldo += valor
        print('Valor depositado com sucesso!!!\n')

    def sacar(self, valor):
        if self.valor_limite < self.saldo:
            self.saldo -= valor
            print('Saque realizado com sucesso!!!\n')
        else:
            print('Saldo insuficiente\n')
            print('você ultrapassou seu limite!!\n')

    def imprimir(self):
        print('Saldo atual:{}\n'.format(self.saldo))


contaco = ContaComum(12345, 'vinicius', 1000)
contaco.imprimir()
contaco.depositar(500)
contaco.sacar(250)
contaco.imprimir()
contaco.sacar(2000)

contap = ContaPoupanca(12345, 'vinicius', 1000, '10/05/2020')
contap.imprimir()
contap.depositar(500)
contap.sacar(250)
contap.imprimir()
contap.sacar(2000)


contal = ContaLimite(12345, 'vinicius', 1000, 3000)
contal.imprimir()
contal.depositar(500)
contal.sacar(250)
contal.imprimir()
contal.sacar(2000)
contal.imprimir()
contal.sacar(2250)
contal.imprimir()
contal.sacar(1)
contal.imprimir()
