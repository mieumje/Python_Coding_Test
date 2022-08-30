def solution(n):
    tmp = ''
    
    while n > 0:
      mod = n % 3
      n = n // 3
      
      tmp = tmp + str(mod)
      
    answer = int(tmp, 3)
    
    return answer

# n   result
# 45  7
# 125 229

n = 125


print(solution(n))
