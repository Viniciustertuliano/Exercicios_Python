selo1 = 20
selo2 = 50
custoMim = 70
custoMax = 620

custo = float(input())
custo = int(custo*100)

while custo%10 !=0 or custo <= custoMim or custo >= custoMax:
    print("Preço invalido, refaça a leitura do pacote")
    custo = float(input())
    custo = int(custo*100)
    print(custo)
qtd50 = custo//selo2
qtd20 = int(custo%selo2)/selo1
print("Compre {} selos(s) de R$ 0.50 e {} selos(s) de R$ 0.20!".format(qtd50,qtd20))