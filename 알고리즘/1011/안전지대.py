def solution(board):
  n = len(board)
  answer = 0
  arr = [[0] * len(board) for _ in range(len(board))]
  dx = [-1, -1, -1, 0, 0, 1, 1, 1]
  dy = [-1, 0, 1, -1, 1, -1, 0, 1]
  
  for x in range(n):
    for y in range(n):
      if board[x][y] == 1:
        arr[x][y] = 1
        for i in range(len(dx)):
          nx, ny = x + dx[i], y + dy[i]
          if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
          arr[nx][ny] = 1
  for i in arr:
    answer += i.count(0)  
  
  return answer

# board	result
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	16
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	13
# [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]	0


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

print(solution(board))