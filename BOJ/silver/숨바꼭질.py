from collections import deque


N, K = map(int, input().split())

q = deque()
cnt = 0
q.append(N)
checked = [0] * 100001

while q:
  X = q.popleft()
  if X == K:
    print(checked[X])
    break
  
  for i in (X - 1, X + 1, 2 * X):
    if 0 <= i < 100001 and checked[i] == 0:
      checked[i] = checked[X] + 1
      q.append(i)