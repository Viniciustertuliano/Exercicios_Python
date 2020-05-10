# -*- coding: utf-8 -*-
class Produto:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.preco = preco
        self.descricao = descricao

    def exibir_descricao(self):
        print('descricão: ', self.descricao)


class Mouse(Produto):
    def __init__(self, nome, preco, descricao, tipo):
        super().__init__(nome, preco, descricao)
        self.tipo = tipo

    def exibir_descricao(self):
        super().exibir_descricao()
        print('Tipo: ', self.tipo)


class Livro(Produto):
    def __init__(self, nome, preco, descricao, autor):
        super().__init__(nome, preco, descricao)
        self.autor = autor

    def exibir_descricao(self):
        super().exibir_descricao()
        print('Autor: ', self.autor)


carrinho = []

m1 = Mouse('Mouse 1', 20.0, 'mouse tipo1', 'Optico USB')
m2 = Mouse('Mouse 2', 30.0, 'mouse Gamer', 'Gamer Optico')
livro1 = Livro('Nome do livro', 30.0,
               'Livro para aprender programação', 'nome do autor ')

carrinho.append(m1)
carrinho.append(m2)
carrinho.append(livro1)

for p in carrinho:
    p.exibir_descricao()
