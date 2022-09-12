n = int(input())

dp = [10008] * 1001

dp[0] = 0
dp[1] = 1
dp[2] = 2

for i in range(n + 1):
  if i < 3: continue
  
  dp[i] = dp[i - 1] + dp[i - 2]
  
answer = dp[n] % 10007

print(answer)