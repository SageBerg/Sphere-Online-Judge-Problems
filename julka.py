def main():
    for i in range(10):
        apples = int(input())
        diff = int(input())
        klaudia = apples // 2
        natalia = apples // 2 
        if diff % 2 == 1:
            klaudia += 1
        klaudia += diff // 2 
        natalia -= diff // 2 
        print(klaudia)
        print(natalia)

main()
