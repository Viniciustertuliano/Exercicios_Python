class Televisao():
    def __init__(self):
        self.canal = None
        self.volume = 0

    def alterar_canal(self, n):
        self.canal = n

    def aumentar_volume(self):
        self.volume += 1

    def diminuir_volume(self):
        self.volume -= 1


tv = Televisao()
tv.alterar_canal(5)
tv.aumentar_volume()
tv.aumentar_volume()
tv.aumentar_volume()
tv.diminuir_volume()
print('canal atual', tv.canal)
print('volume', tv.volume)
