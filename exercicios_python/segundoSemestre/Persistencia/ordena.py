impar = open('impares.txt', 'r')
par = open('pares.txt', 'r')
novo = []

for linha in impar:
    novo.append(int(linha))

for linha in par:
    novo.append(int(linha))

novo.sort()

ordenado = open('ordenado.txt', 'a')
for i in novo:
    ordenado.write('{}\n'.format(i))

ordenado.close()
impar.close()
par.close()
