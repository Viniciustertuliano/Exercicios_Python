# -*- coding: utf-8 -*-
class Veiculo:
    def __init__(self):
        pass

    def limpar(self):
        pass

    def consertar(self):
        pass


class Bicicleta:
    def __init__(self):
        super().__init__()

    def limpar(self):
        print('Bicicleta foi limpo')

    def consertar(self):
        print('Bicicleta foi consertado')


class Automovel:
    def __init__(self):
        super().__init__()

    def limpar(self):
        print('Automóvel foi limpo')

    def consertar(self):
        print('Automóvel foi consertado')

    def trocar_oleo(self):
        print('O óleo foi trocado')


bike = Bicicleta()
carro = Automovel()

bike.limpar()
bike.consertar()

carro.limpar()
carro.consertar()
carro.trocar_oleo()
