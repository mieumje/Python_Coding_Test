def solution(n):
  answer = 0
  sum = 0
  
  for i in range(n):
    for j in range(i + 1, n + 1):
      sum += j
      if sum > n:
        sum = 0
        break
      
      if sum == n:
        sum = 0
        answer += 1
        break

  return answer


# n	  result
# 15	4

n = 15

print(solution(n))
