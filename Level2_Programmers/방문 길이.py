def solution(dirs):
  arr = [[0] * 11 for _ in range(11)]
  arr[5][5] = 1
  answer = 0
  cur_x, cur_y = 5, 5
  dx = [-1, 1, 0, 0] # 상, 하, 좌, 우 
  dy = [0, 0, -1, 1] # 상, 하, 좌, 우
  
  for dir in dirs:
    nx, ny = 0, 0
    if dir == 'U':
      nx = cur_x + dx[0]
      ny = cur_y + dy[0]
    elif dir == 'D':
      nx = cur_x + dx[1]
      ny = cur_y + dy[1]
    elif dir == 'L':
      nx = cur_x + dx[2]
      ny = cur_y + dy[2]
    elif dir == 'R':
      nx = cur_x + dx[3]
      ny = cur_y + dy[3]
    if nx < 0 or ny < 0 or nx > 10 or ny > 10:
      continue
    if arr[nx][ny] == 0:
      arr[nx][ny] = 1
      answer += 1

    cur_x, cur_y = nx, ny

  if dirs[0] == "U" or dirs[0] == "D":
    answer += 1  
  return answer

# dirs	      answer
# "ULURRDLLU"	7
# "LULLLLLLU"	7

dirs = "ULURRDLLU"

print(solution(dirs))