import math
def solution(n, k):
  arr = [i for i in range(1, n + 1)]
  answer = []
  
  while n > 0:
    n -= 1
    div, mod = divmod(k, math.factorial(n))
    
    if mod == 0:
      div -= 1
    answer.append(arr.pop(div))
    k = mod
    
  return answer

# n	k	result
# 3	5	[3,1,2]

n = 3
k = 5
print(solution(n, k))
