def solution(n):
  answer = []
  tmp = [[0] * n for _ in range(n)]
  num = 0
  x, y = -1, 0
  
  for i in range(n, 0, -3):
    for _ in range(1, i + 1):
      x += 1
      num += 1
      tmp[x][y] = num
    for _ in range(1, i):
      y += 1
      num += 1
      tmp[x][y] = num
    for _ in range(1, i - 1):
      x -= 1
      y -= 1
      num += 1
      tmp[x][y] = num
  
  answer = [item for i in tmp for item in i if item != 0]
  
  return answer

# n	result
# 4	[1,2,9,3,10,8,4,5,6,7]
# 5	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]

def reverse_solution(n):
  tmp = [[0] * n for _ in range(n)]
  num = 0
  x, y = -1, -1

  for i in range(n, 0, -3):
    for _ in range(1, i + 1):
      x += 1
      y += 1
      num += 1
      tmp[x][y] = num
    for _ in range(1, i):
      y -= 1
      num += 1
      tmp[x][y] = num
    for _ in range(1, i - 1):
      x -= 1
      num += 1
      tmp[x][y] = num
  
  answer = [item for i in tmp for item in i if item != 0]
  
  return answer

for i in range(4, 6):
  print(solution(i))
  print(reverse_solution(i))
