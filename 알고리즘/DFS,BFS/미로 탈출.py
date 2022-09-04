from collections import deque

def solution(n, m, graph):
  answer = -1
  x, y = 0, 0
  dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
  
  queue = deque()
  queue.append((x, y))
  
  while queue:
    x, y = queue.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if graph[nx][ny] == 0:
        continue
      
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  
  answer = graph[-1][-1]
  return answer

n = 5
m = 6
graph = [
  [1, 0, 1, 0, 1, 0],
  [1, 1, 1, 1, 1, 1],
  [0, 0, 0, 0, 0, 1],
  [1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1],
]

print(solution(n, m, graph))