class Carro():
    def __init__(self, con):
        self.consumo = con
        self.quantidade_combustivel = 0

    def adicionar_combustivel(self, com):
        comb = com
        self.quantidade_combustivel += comb
        return self.quantidade_combustivel

    def obter_combustivel(self):
        return self.quantidade_combustivel

    def andar(self, di):
        dis = di
        con = self.consumo
        gas = self.quantidade_combustivel
        for i in range(con):
            for a in range(dis):
                print(a)
            gas -= 1
            return gas


t = Carro(2)
t.adicionar_combustivel(10)
t.andar(2)
print(t.obter_combustivel())
