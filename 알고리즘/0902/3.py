import math

def solution(n, k):
    answer = 0
    rev_base = ''
    
    while n > 0:
      n, mod = divmod(n, k)
      rev_base += str(mod)
      
    rev_base = rev_base[::-1]
    
    tmp = ''
    arr = rev_base.split('0')
    
    def check_prime(numb):
      if numb == 1:
        return False
      if numb == 2:
        return True
      
      root = int(math.sqrt(numb) + 1)
      
      for i in range(2, root):
        if numb % i == 0:
          return False
        
      return True
    
    for i in arr:
      if i == '': continue
      if check_prime(int(i)):
        answer += 1   
    
    return answer
  
# n	      k	  result
# 437674	3	  3
# 110011	10	2

n = 110011
k = 10

print(solution(n, k))
