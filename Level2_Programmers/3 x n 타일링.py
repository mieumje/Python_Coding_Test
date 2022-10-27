def solution(n):
  answer = 0
  if n % 2 == 1:
    return 0
  
  dp = [0] * 5001
  dp[2] = 3
  dp[4] = 11
  
  if n == 2 or n == 4:
    return dp[n]
  
  for i in range(6, n + 1):
    if i % 2 == 1: continue
    
    tmp = dp[2:i:2]
    dp[i] = tmp[-1] * 3
  
    for x in tmp[:-1]:
      dp[i] += x * 2
    
    dp[i] += 2
    dp[i] = dp[i] % 1000000007

  answer = dp[n]
  
  return answer

# n	result
# 4	11

print(solution(n=8))
