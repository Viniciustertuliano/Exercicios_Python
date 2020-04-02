class Triangulo():
    def __init__(self):
        self.lado_a = 0
        self.lado_b = 0
        self.lado_c = 0

    def calcular_perimetro(self):
        print(self.lado_a + self.lado_b + self.lado_c)

    def maior_lado(self):
        if (self.lado_a > self.lado_b):
            if(self.lado_a > self.lado_c):
                print(self.lado_a)
            else:
                print(self.lado_c)

        elif(self.lado_b > self.lado_c):
            print(self.lado_b)
        else:
            print(self.lado_c)
