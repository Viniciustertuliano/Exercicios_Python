#Escreva as seguintes expressões matemáticas utilizando operadores e funções vistas nessa
#aula:
#a) 3x y xy
#3 2 − 52
#b) x = 2a−b±√b −4ac2
#c) y = log3x e π 2 + e + π + e

import math

x = int(input("Digite o valor de X:"))
y = int(input("Digite o valor de y:"))
a = int(input("Digite o valor de a:"))
b = int(input("Digite o valor de b:"))
c = int(input("Digite o valor de c:"))

rest1 = 3 * math.pow(x,3) * math.pow(y,2) - 5 * x * math.pow(y,2)
x1 = ( - b + (math.pow(b,2) - (4 * a * c)) ** 0.5) / 2 * a
x2 = ( - b - (b ** 2 - (4 * a * c))** 0.5)/ 2 * a
y1 = math.log(x**2,3) + math.e + math.exp(math.pi) + math.pi ** math.e



print("\nO resultado é: ", rest1, "\nO bascara é: ", "x: ", x1, "e", "x: ", x2, "\n resultado é: ", y1)