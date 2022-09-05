x = int(input())

dp = [0] * 30001

# dp[0] = 0, dp[1] = 0
# 2부터 dpP에 기록
# 최종 dpp[x]를 찾는다

for i in range(2, x + 1):
  dp[i] = dp[i - 1] + 1 # 1을 뺀 경우
  
  if i % 2 == 0:
    dp[i] = min(dp[i], dp[i // 2] + 1)
    
  if i % 3 == 0:
    dp[i] = min(dp[i], dp[i // 3] + 1)
    
  if i % 5 == 0:
    dp[i] = min(dp[i], dp[i // 5] + 1)
    
print(dp[x])