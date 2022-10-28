from math import factorial


t = int(input())

for i in range(t):
  n, m = map(int, input().split())
  answer = factorial(m) // (factorial(n) * factorial(m - n))
  print(answer)