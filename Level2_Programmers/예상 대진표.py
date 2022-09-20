import math

def solution(n,a,b):
  answer = 0
  
  if a % 2 != 0 and a + 1 == b:
    return answer + 1
    
  if a % 2 == 0 and a - 1 == b:
    return answer + 1
  
  while True:
    if n == 1: break
    n = n // 2
    a = math.ceil(a / 2)
    b = math.ceil(b / 2)
    answer += 1
    
    if a % 2 != 0 and a + 1 == b:
      break
    
    if a % 2 == 0 and a - 1 == b:
      break
  
  return answer + 1

# N	A	B	answer
# 8	4	7	3

print(solution(n=8, a=4, b=7))
