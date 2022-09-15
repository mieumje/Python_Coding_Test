def solution(A,B):
  answer = 0
  A.sort()
  B.sort(reverse = True)

  length = len(A)
  
  for i in range(length):
    answer += A[i] * B[i]

  return answer

# A	        B	        answer
# [1, 4, 2]	[5, 4, 4]	29
# [1,2]	    [3,4]	    10

A = [1, 4, 2]
B = [5, 4, 4]

print(solution(A, B))