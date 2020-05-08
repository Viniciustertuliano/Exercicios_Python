class Filme():
    def __init__(self, titulo, genero):
        self.__titulo = titulo
        self.__genero = genero

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero


lista = []
for i in range(3):
    titulo = input("Titulo: ")
    genero = input("Genero: ")
    filme = Filme(titulo, genero)
    lista.append(filme)

for i in lista:
    print("Titulo do filme: {}, O genero do filme: {}".format(
          i.get_titulo(), i.get_genero()))
