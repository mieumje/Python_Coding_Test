def solution(n):
  answer = 0
  dp = [0] * 3
  dp[0] = 0
  dp[1] = 1
  dp[2] = 2
    
  for i in range(n + 1):
      if i < 3: continue
        
      dp.append((dp[i - 1] + dp[i - 2]) % 1000000007) 
  
  answer = dp[n]
    
  return answer
  
print(solution(n=4))
