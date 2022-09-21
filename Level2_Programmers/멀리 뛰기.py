def solution(n):
  answer = 0
  
  dp = [0] * 2001
  dp[1] = 1
  dp[2] = 2
  
  if n < 3:
    answer = dp[n] % 1234567
    return answer
  
  for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  
  answer = dp[n] % 1234567
  
  return answer

# n	result
# 4	5
# 3	3

print(solution(n = 4))
print(solution(n = 3))