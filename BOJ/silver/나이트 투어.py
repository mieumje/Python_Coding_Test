def knight_tour(tracks):
  def check_distance(ax, ay, bx, by):
    if abs(ax - bx) > 2 or abs(ay - by) > 2:
      return False
    elif abs(ax - bx) == 2 and abs(ay - by) != 1:
      return False
    elif abs(ax - bx) == 1 and abs(ay - by) != 2:
      return False
    return True
  
  visited = [[False] * 6 for _ in range(6)]
  start_x, start_y = ord(tracks[0][0]) - 65, int(tracks[0][1]) - 1
  last_x, last_y = ord(tracks[-1][0]) - 65, int(tracks[-1][1]) - 1
  
  if not check_distance(start_x, start_y, last_x, last_y):
    return 'Invalid'
  
  visited[start_x][start_y] = True
  curr_x, curr_y = start_x, start_y
  
  for i in range(1, 36):
    next_x, next_y = ord(tracks[i][0]) - 65, int(tracks[i][1]) - 1
    if visited[next_x][next_y] == True or not check_distance(curr_x, curr_y, next_x, next_y):
      return 'Invalid'

    visited[next_x][next_y] = True
    curr_x, curr_y = next_x, next_y

  return 'Valid'

tracks = [input() for _ in range(36)]
print(knight_tour(tracks))
