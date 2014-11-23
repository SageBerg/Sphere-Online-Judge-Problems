n = int(input())

for i in range(n):
  a, b = input().split(" ")
  a = a[::-1]
  b = b[::-1]
  a = int(a)
  b = int(b)
  c = a + b
  c = str(c)
  c = c[::-1]
  c = c.strip("0")
  print(c)
