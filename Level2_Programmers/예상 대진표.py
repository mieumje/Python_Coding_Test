import math

def solution(n,a,b):
  answer = 0
  if b % 2 == 0 and b - 1 == a:
    answer += 1
    return answer
  while True:
    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    answer += 1
    if abs(a - b) == 1:
      break
  
  return answer + 1

# N	A	B	answer
# 8	4	7	3

print(solution(n=8, a=4, b=7))
