class Funcionario():
    def __init__(self):
        self.nome = ''
        self.salario = 0.0

    def aumenta_salario(self, porc):
        adicional = self.salario * porc
        final = self.salario + adicional
        print('{} O valor atual do seu salario é: {}'.format(self.nome, final))
