n, m = map(int, input().split())

array = []

for i in range(n):
  array.append(int(input()))

array.sort()

dp = [10001 for _ in range(m + 1)]
dp[0] = 0

for i in range(m + 1):
  for j in array:
    if i - j < 0: continue
    dp[i] = min(dp[i], dp[i - j] + 1)
    
answer = -1 if dp[m] > 10000 else dp[m]    

print(answer)