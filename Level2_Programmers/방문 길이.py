def solution(dirs):
  arr = [[0] * 11 for _ in range(11)]
  arr[5][5] = 1
  answer = 0
  cur_x, cur_y = 0, 0
  dx = [0, 0, -1, 1] # 상, 하, 좌, 우 
  dy = [1, -1, 0, 0] # 상, 하, 좌, 우
  record = []
  
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
    
    if nx < -5 or ny < -5 or nx > 5 or ny > 5:
      continue
    tmp = [(cur_x, cur_y), (nx, ny)]
    
    if tmp not in record:
      answer += 1
      record.append(tmp)
    
    cur_x, cur_y = nx, ny
  
  return answer

# dirs	      answer
# "ULURRDLLU"	7
# "LULLLLLLU"	7

dirs = "LULLLLLLU"

print(solution(dirs))
