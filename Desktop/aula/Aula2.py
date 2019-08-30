import math

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
x = float(input('Digite o valor de x: '))

y_pot = (a**2+(3*b)**(1/2))/(5*x**3)
y_raiz = (a**2+math.sqrt(3*b))/(5*x**3)

if (y_pot == y_raiz):
 print(y_pot)
 print(y_raiz)


x2 = y_pot + (2*b/(a+b))**0.5

print('item , b x =', x2 )