N = int(input())
arr = [0]
for _ in range(N):
  arr.append(int(input()))
dp = [0] * (N + 1)
dp[1] = arr[1]
dp[2] = max(arr[2], dp[1] + arr[2])

for i in range(3, N + 1):
  dp[i] = max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3])
  
print(dp[-1])