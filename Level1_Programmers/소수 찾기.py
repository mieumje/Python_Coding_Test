import math
def is_prime(n):
    sqrt_n = math.sqrt(n)
    round_sqrt_n = math.ceil(sqrt_n)
    for i in range(2, round_sqrt_n+1):
        if(n % i == 0):
            return False
    
    return True

def solution(n):
    answer = 0
    if(n == 1): return 0
    if(n == 2): return 1
    
    for i in range(3,n+1,2):
        if(is_prime(i)):
            print(i)
            answer += 1
    if(n>=2): answer += 1
    
    return answer

n = 5
print(solution(n))