def solution(n, left, right):
  answer = []
  arr = [[0] * (n + 1) for _ in range(n + 1)]
  
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      maximum = max(i, j)
      arr[i][j] = maximum
 
  for i in range(1, n + 1):
    answer += arr[i][1:]

  answer = answer[left : right + 1]  
  
  return answer

# n	  left	right	  result
# 3	  2	    5	      [3,2,2,3]
# 4	  7	    14	    [4,3,3,3,4,4,4,4]

n = 4
left = 7
right = 14

print(solution(n, left, right))
