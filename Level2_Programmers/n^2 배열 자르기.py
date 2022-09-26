def solution(n, left, right):
  answer = []
  arr = [[max(i, j + 1) for i in range(n + 1)] for j in range(n + 1)]
 
  for i in range(n):
    answer += arr[i][1:]

  answer = answer[left : right + 1]
  
  return answer

# n	  left	right	  result
# 3	  2	    5	      [3,2,2,3]
# 4	  7	    14	    [4,3,3,3,4,4,4,4]

n = 3
left = 2
right = 5

print(solution(n, left, right))