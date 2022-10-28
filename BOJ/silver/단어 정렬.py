N = int(input())
arr = []
for _ in range(N):
  word = input()
  arr.append((word, len(word)))

arr = sorted(set(arr), key = lambda x : (x[1], x[0]))

for k, v in arr:
  print(k)
