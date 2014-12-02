def fac(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod

for i in range(int(input())):
    print(fac(int(input())))
