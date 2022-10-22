from collections import defaultdict, deque


def solution(n, wires):
  answer = float('inf')
  lists = defaultdict(list)
  
  def dfs_count(wire, n, lists):
    cnt = 1
    visited = [False] * (n + 1)
    curr, delete_node = wire
    q = deque([])
    q.append(curr)
    visited[curr] = True
    
    while q:
      nodes = q.popleft()
      for i in lists[nodes]:
        if visited[i] or i == delete_node:
          continue
        cnt += 1
        q.append(i)
        visited[i] = True
      print(q)
    return cnt

  for i, j in wires:
    lists[i].append(j)
    lists[j].append(i)
  
  for wire in wires:
    cnt = dfs_count(wire, n, lists)
    rest = n - cnt
    answer = min(answer, abs(rest - cnt))
  
  return answer

# n	wires	                                            result
# 9	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	3
# 4	[[1,2],[2,3],[3,4]]	                              0
# 7	[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]	            1

n = 4
wires = [[1,2],[2,3],[3,4]]
print(solution(n, wires))