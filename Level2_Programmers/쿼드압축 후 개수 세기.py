def solution(arr):
  answer = [0, 0]
  length = len(arr)
  
  def quad(x, y, length):
    flag = arr[x][y]
    
    for i in range(x, x + length):
      for j in range(y, y + length):
        if arr[i][j] != flag:
          length //= 2
          quad(x, y, length)
          quad(x, y + length, length)
          quad(x + length, y, length)
          quad(x + length, y + length, length)
          return
    answer[flag] += 1
  
  quad(0, 0, length)
  
  return answer

# arr	                  result
# [ [1,1,0,0],
#   [1,0,0,0],
#   [1,0,0,1],
#   [1,1,1,1] ]         [4,9]
# [ [1,1,1,1,1,1,1,1],
#   [0,1,1,1,1,1,1,1],
#   [0,0,0,0,1,1,1,1],
#   [0,1,0,0,1,1,1,1],
#   [0,0,0,0,0,0,1,1],
#   [0,0,0,0,0,0,0,1],
#   [0,0,0,0,1,0,0,1],
#   [0,0,0,0,1,1,1,1] ]	[10,15]

arr = [ [1,1,0,0],
  [1,0,0,0],
  [1,0,0,1],
  [1,1,1,1] ]

print(solution(arr))
