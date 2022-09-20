def solution(N, fees, dest):
  global cnt
  answer = 0
  cnt = 0
  
  arr = [[None] * (N + 1) for _ in range(N + 1)]
  
  
  for i in fees:
    A, B, fee = i 
    arr[A][B], arr[B][A] = fee, fee
  
  visited = [[False] * (N + 1) for _ in range(N + 1)]
  
  
  
  def dfs(arr, visited, index, sum):
    x, y = index
    visited[x][y] = True
    print(index, sum)
    
    for i in range(1, len(arr)):
      for j in range(1, len(arr[i])):
        if arr[i][j] == None: continue
        if arr[i][j] != None and visited[i][j] != True:
          sum += arr[i][j]
          
          dfs(arr, visited, [i,j], sum)
  sum = 0
  dfs(arr, visited, [1, 1], sum)
  
  return answer

# N   fees                                                                                  dest
# 5   [[1, 2, 1000], [1, 5, 2000], [2, 3, 3000], [2, 4, 1500], [3, 4, 1000], [4, 5, 2000]]  3

print(solution(N=5, fees=[[1, 2, 1000], [1, 5, 2000], [2, 3, 3000], [2, 4, 1500], [3, 4, 1000], [4, 5, 2000]], dest=3))