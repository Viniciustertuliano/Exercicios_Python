import ex_11

tup1 = ()
tup2 = ()

for i in range(3): 
    tup1 += (int(input("digite o valor da tupla 1º: ")),) 

for i in range(3): 
    tup2 += (int(input("digite o valor da tupla 2º: ")),) 

print(ex_11.intercala(tup1, tup2))