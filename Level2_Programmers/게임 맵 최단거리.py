def solution(maps):
  answer = 0
  n, m = len(maps), len(maps[-1])
  cur_x, cur_y = 0, 0
  checked = [[1000001] * n for i in range(m)]
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  checked[0][0] = 1
  
  def dfs(x, y, checked, cnt):
    checked[x][y] = cnt

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if nx < 0 or ny < 0 or nx >= n or ny >= m:
        continue
      
      if maps[nx][ny] == 1 and checked[nx][ny] > cnt + 1:
        dfs(nx, ny, checked, cnt + 1)

  
  dfs(cur_x, cur_y, checked, cnt = 1)

  answer = checked[-1][-1] if checked[-1][-1] != 1000001 else -1
  return answer

# maps	                                                        answer
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]	11
# [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	-1

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))