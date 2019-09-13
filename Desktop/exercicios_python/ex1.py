n1 = int (input("Digite o prineiro valor: "))
n2 = int (input("Digite o segundo valor: "))
#função de somar #
def soma (n1, n2):
    va1 = n1
    va2 = n2
    return  va1 + va2

print("A soma de ", n1,"e ",n2,"é: ", soma(n1,n2))

#função de subtrair#
def sub (n1,n2):
    va1 = n1
    va2 = n2
    return va1 - va2 

print("A subtração de ",n1,"e ",n2,"é: ", sub(n1,n2))

#função de multiplicar 

def mult (n1, n2):
    va1 = n1
    va2 = n2
    return va1 * va2

print("A multiplicação de ",n1,"e ",n2,"é: ", mult(n1,n2))

#função de divisão 

def div (n1, n2):
    va1 = n1
    va2 = n2
    return va1 / va2

print("A divisão de ",n1,"e ",n2,"é: ", div(n1,n2))

#função de divisão truncada

def div_tru (n1, n2):
    va1 = n1
    va2 = n2
    return va1 // va2

print("A divisão truncada de ",n1,"e ",n2,"é: ", div_tru(n1,n2))

#função de divisão truncada

def div_rest (n1, n2):
    va1 = n1
    va2 = n2
    return va1 % va2

print("O resto da divisão de ",n1,"e ",n2,"é: ", div_rest(n1,n2))

#função de exponenciação

def exp (n1, n2):
    va1 = n1
    va2 = n2
    return va1 ** va2

print("A exponenciação de ",n1,"e ",n2,"é: ", exp(n1,n2))