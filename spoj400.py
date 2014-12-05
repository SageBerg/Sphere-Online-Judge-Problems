"""
SPOJ 400: To and Fro
Sage Berg
4 Dec 2014
"""

def slow_decrypt(cols, string):
    decrypted = ""
    rows = len(string)//cols
    grid = list()
    for _ in range(rows):
        grid.append(list())
    row = 0
    i = 0
    while i < len(string):
        if row%2 == 0:
            while len(grid[row]) < cols:
                grid[row].append(string[i])
                i += 1
        else:
            while len(grid[row]) < cols:
                grid[row].insert(0, string[i])
                i += 1
        row += 1
    for col in range(cols):
        for row in grid:
            print(row[col], end="")
    print()

def main():
    while True:
        cols = int(input())
        if cols != 0:
            string = input()
            slow_decrypt(cols, string)
        else:
            break

main()
