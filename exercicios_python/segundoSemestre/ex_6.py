def divisores(n):
    r = 0
    for i in range(1, n+1):
        if (n % i) == 0:
            r = r + i
    print(r)


divisores(int(input("digite o numero: ")))
