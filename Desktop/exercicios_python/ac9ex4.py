n = input()
a = input().split(" ")
n2 = input()
b = input().split(" ")


for x in b:
    if x in a:
        print(1)
        break
    else:
        print(0)
        break