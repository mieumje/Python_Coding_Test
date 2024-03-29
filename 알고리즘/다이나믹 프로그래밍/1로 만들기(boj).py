n = int(input())

dp = 10000001 * [10000001]

dp[0] = None
dp[1] = 0
dp[2] = 1
dp[3] = 1



for i in range(1, n + 1):
  if i < 4: continue
  
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)
  
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
  
  dp[i] = min(dp[i], dp[i - 1] + 1)
  
print(dp[n])