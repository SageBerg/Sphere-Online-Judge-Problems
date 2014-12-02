def fact_trailing_zeros(n):
    answer = 0
    power = 1
    while n >= 5**power:
        answer += n//(5**power)
        power += 1
    return answer

inputs = int(input())
for i in range(inputs):
   print(fact_trailing_zeros(int(input())))
