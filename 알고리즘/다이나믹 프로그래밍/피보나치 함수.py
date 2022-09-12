T = int(input())

arr = []

fibo = [[0, 0] for _ in range(41)]
fibo[0] = [1, 0]
fibo[1] = [0, 1]

for i in range(T):
  arr.append(int(input()))

last_idx = max(arr)

for i in range(last_idx + 1):
  if i == 0 or i == 1:
    continue
  
  x = fibo[i - 1][0] + fibo[i - 2][0]
  y = fibo[i - 1][1] + fibo[i - 2][1]
  fibo[i] = [x, y]
  

for i in arr:
  x, y = fibo[i]
  print(x, y)
  
  