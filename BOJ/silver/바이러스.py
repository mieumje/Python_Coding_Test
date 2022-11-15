from collections import deque

nums_com = int(input())
N = int(input())
visited = [False] * (nums_com + 1)

computers = [[] for _ in range(nums_com + 1)]

for i in range(N):
  x, y = map(int, input().split())
  computers[x].append(y)
  computers[y].append(x)
  
q = deque()
q.append(1)

answer = -1

while q:
  tmp = q.popleft()
  if not visited[tmp]:
    answer += 1
    visited[tmp] = True
    for i in computers[tmp]:
      if not visited[i]:
        q.append(i)
        
print(answer)