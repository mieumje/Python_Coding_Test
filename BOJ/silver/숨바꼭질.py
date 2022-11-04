from collections import deque


N, K = map(int, input().split())

q = deque()
cnt = 0
q.append((N, cnt))

while q:
  X, cnt = q.popleft()
  if X == K:
    print(cnt)
    break
  cnt += 1
  
  for i in range(3):
    if i == 0:
      nx = X - 1
    elif i == 1:
      nx = X + 1
    else:
      nx = 2 * X
    q.append((nx, cnt))