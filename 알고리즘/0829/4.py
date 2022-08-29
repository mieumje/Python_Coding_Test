def solution(board, skill):
  answer = 0
  tmp = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
  
  for type, r1, c1, r2, c2, degree in skill:
    degree = degree if type == 2 else -degree
    
    tmp[r1][c1] += degree
    tmp[r1][c2 + 1] += -degree
    tmp[r2 + 1][c1] += -degree
    tmp[r2 + 1][c2 + 1] += degree
  
  for x in range(len(tmp) - 1): # row
    for y in range(len(tmp[0]) - 1):
      tmp[x][y + 1] += tmp[x][y]
 
  for y in range(len(tmp[0]) - 1): # col
    for x in range(len(tmp) - 1):
      tmp[x + 1][y] += tmp[x][y]
 
  for x in range(len(board)):
    for y in range(len(board[0])):
      board[x][y] += tmp[x][y]     
      if board[x][y] > 0: answer += 1
 
  return answer
  
board = [
  [5,5,5,5,5],
  [5,5,5,5,5],
  [5,5,5,5,5],
  [5,5,5,5,5]
]

skill = [
  [1,0,0,3,4,4],
  [1,2,0,2,3,2],
  [2,1,0,3,1,2],
  [1,0,1,3,3,1]
]

result = 10

print(solution(board, skill))