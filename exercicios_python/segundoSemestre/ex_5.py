def divisores(n):
    for i in range(1,n+1):
        if (n % i) == 0:
            print(i)

divisores(int(input("digite o numero: ")))
