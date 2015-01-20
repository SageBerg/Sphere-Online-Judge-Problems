def main():
    for _ in range(int(input())):
        blank_line = input()
        candy_sum = 0
        children = int(input())
        for c in range(children):
            candy_sum += int(input()) 
        if candy_sum % children == 0:
            print("YES")
        else:
            print("NO")
main()
