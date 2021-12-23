import math
def is_prime(n):
    if(n == 2):
        return True

    sqrt_n = math.sqrt(n)
    round_sqrt_n = math.ceil(sqrt_n)
    for i in range(2, round_sqrt_n+1):
        if(n % i == 0):
            return False
    
    return True

def solution(n):
    answer = 0
    for i in range(2,n+1):
        if(is_prime(i)):
            print(i)
            answer += 1
    
    return answer

n = 10
print(solution(n))
