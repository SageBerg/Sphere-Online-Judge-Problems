"""
SPOJ 1112: Number Steps
Sage Berg
2 Dec 2014
"""

def num_at_coords(x, y):
    answer = "No Number"
    if x == y:
        answer = 4 * (x // 2)
    elif x == y + 2:
        answer = 4 * (x // 2) - 2
    if answer != "No Number" and x % 2 != 0:
        answer += 1
    print(answer)

n = int(input())
for i in range(n):
    x, y = input().split()
    num_at_coords(int(x), int(y))
