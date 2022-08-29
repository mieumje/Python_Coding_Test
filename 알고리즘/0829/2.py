def solution(a, b):
    answer = 0
    length = len(a)
    
    for i in range(0, length):
      answer += a[i] * b[i];
    return answer
  
  
# a         b           result
# [1,2,3,4] [-3,-1,0,2] 3
# [-1,0,1]  [1,0,-1]    -2

a = [1,2,3,4]
b = [-3,-1,0,2]

print(solution(a,b))