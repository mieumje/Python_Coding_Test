from collections import defaultdict, deque


N, M, V = map(int, input().split())

arr = []

for _ in range(M):
  x, y = map(int, input().split())
  arr.append([x, y])
arr = sorted(arr, key = lambda x : (x[0], x[1]))
print(arr)
lists = defaultdict(list)  
for i in arr:
  x, y = i
  lists[x].append(y)
  lists[y].append(x)
print(lists)

def dfs(node, lists, visited):
  visited[node] = True
  print(node, end = ' ')
  for i in lists[node]:
    if not visited[i]:
      dfs(i, lists, visited)

def bfs(node, lists, visited):
  visited[node] = True
  q = deque([])
  q.append(node)
  while q:
    curr = q.popleft()
    print(curr, end = ' ')
    for i in lists[curr]:
      if not visited[i]:
        visited[i] = True
        q.append(i)

dfs(V, lists, visited = [False] * (N + 1))
print('')     
bfs(V, lists, visited = [False] * (N + 1))
