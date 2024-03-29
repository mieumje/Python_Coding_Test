def solution(n):
  answer = 0
  
  dp = [0] * 100001
  
  dp[0] = 0
  dp[1] = 1
  
  
  for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
  
  answer = dp[n] % 1234567
  
  return answer

# n	return
# 3	2
# 5	5

n = 5

print(solution(n))