from collections import deque


N, M = map(int, input().split())

visited = [[0] * N for _ in range(M)]
arr = []

for _ in range(N):
  line = input()
  tmp = []
  for i in line:
    tmp.append(int(i))
  arr.append(tmp)
  
q = deque()
q.append((0, 0))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

while q:
  x, y = q.popleft()
  
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if nx < 0 or ny < 0 or nx >= N or ny >= M:
      continue
    
    if arr[nx][ny] == 0:
      continue
    
    if arr[nx][ny] == 1:
      arr[nx][ny] = arr[x][y] + 1
      q.append((nx, ny))
      
print(arr[-1][-1])