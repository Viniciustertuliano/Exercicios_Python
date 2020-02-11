idade,cont, contIdade, mediaIdade = 0,1,0,0


while cont > 0 :
    idade = int(input("Informe a idade:"))
    
    mediaIdade += idade
    contIdade += 1
    if idade == 0:
        cont = -1
        contIdade -= 1
        
mediaIdade /= contIdade   
print("Média das idades é:{:.0f}".format(mediaIdade) )