def solution(board):
  answer = 0
  
  dp = [[0 for _ in range(len(board[0]) + 1)] for _ in range(len(board) + 1)]
  
  for i in range(len(board[0])):
    dp[1][i + 1] = board[0][i]
  for i in range(len(board)):
    dp[i + 1][1] = board[i][0]

  for i in range(1, len(board) + 1):
    for j in range(1, len(board[0]) + 1):
      if board[i - 1][j - 1] == 1:
        dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        answer = max(answer, dp[i][j])
    
  answer *= answer
  
  return answer

# board	                                    answer
# [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	9
# [[0,0,1,1],[1,1,1,1]]	                    4

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

print(solution(board))