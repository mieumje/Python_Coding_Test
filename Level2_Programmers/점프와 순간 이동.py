import math

def solution(n):
  ans = 0
  
  dp = [math.inf] * 100000001
  dp[1] = 1
  dp[2] = 1
  
  if n < 3:
    return dp[n]
  for i in range(3, n + 1):
    for j in range(i // 2, i):
      if j == i // 2 and i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2])
      else:
        dp[i] = min(dp[i], dp[j] + i - j)

  ans = dp[n]
  return ans

# N	    result
# 5	    2
# 6	    2
# 5000	5


print(solution(6))
print(solution(5))
print(solution(5000))