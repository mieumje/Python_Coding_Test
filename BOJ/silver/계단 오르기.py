N = int(input())
arr = []
dp = []
for _ in range(N):
  arr.append(int(input()))

if N <= 2:
  print(sum(arr))
else:
  dp.append(arr[0])
  dp.append(max(arr[1], arr[0] + arr[1]))
  dp.append(max(arr[2] + arr[1], arr[2] + arr[0]))
  for i in range(3, N):
    dp.append(max(arr[i] + dp[i - 2], arr[i] + arr[i - 1] + dp[i - 3]))
  print(dp.pop())