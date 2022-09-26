def solution(n, left, right):
  answer = []
  
  for i in range(left, right + 1):
    ans = max(i // n, i % n) + 1
    answer.append(ans)
  
  return answer

# n	  left	right	  result
# 3	  2	    5	      [3,2,2,3]
# 4	  7	    14	    [4,3,3,3,4,4,4,4]

n = 4
left = 7
right = 14

print(solution(n, left, right))
