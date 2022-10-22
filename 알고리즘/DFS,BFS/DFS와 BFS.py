from collections import defaultdict, deque


N, M, V = map(int, input().split())

g = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
  x, y = map(int, input().split())
  g[x][y] = 1
  g[y][x] = 1

def dfs(node, visited):
  visited[node] = True
  print(node, end = ' ')
  for i in range(len(g[node])):
    if not visited[i] and g[node][i] == 1:
      dfs(i, visited)

def bfs(node, visited):
  visited[node] = True
  q = deque([])
  q.append(node)
  while q:
    curr = q.popleft()
    print(curr, end = ' ')
    for i in range(len(g[curr])):
      if not visited[i] and g[curr][i] == 1:
        visited[i] = True
        q.append(i)

dfs(V, visited = [False] * (N + 1))
print('')     
bfs(V, visited = [False] * (N + 1))
