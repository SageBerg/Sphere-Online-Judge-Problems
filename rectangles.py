def main():
    squares = int(input())
    i = 1
    recs = 0
    while i * i <= squares:
        recs += ((squares // i) - (i - 1))
        i += 1
    print(recs)

main()
