def solution(n):
  answer = 0
  dp = [1000008] * 60000
  dp[0] = 0
  dp[1] = 1
  dp[2] = 2
    
  for i in range(n + 1):
      if i < 3: continue
        
      dp[i] = dp[i - 1] + dp[i - 2]
  
  answer = dp[n] % 1000000007
    
  return answer
  
print(solution(n=4))