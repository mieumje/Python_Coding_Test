def solution(k, d):
  import math
  answer = 0

  for i in range(d + 1):
    for j in range(d + 1):
      if i * k > d or j * k > d:break
      a = i * k
      b = j * k
      distance = math.sqrt(a**2 + b**2)
      if not distance > d:
        answer += 1
  
  return answer

# k	d	result
# 2	4	6
# 1	5	26

k = 1
d = 5

print(solution(k, d))