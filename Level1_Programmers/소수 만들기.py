"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return
"""
from itertools import combinations

def is_prime(num):
    for i in range(2, num):
        check_prime = 0
        if num % i == 0:
            check_prime = 1 # 소수가 아님
            break
    
    if check_prime != 0: # 소수가 아닐 때 0 return
        return 0
    else:               # 소수이면 1 return
        return 1

def solution(nums):
    answer = 0
    
    b = list(combinations(nums, 3)) # nums 중 3개로 조합할 수 있는 숫자
    
    for i in range(0, len(b)):
        x = b[i][0] + b[i][1] + b[i][2]
        result = is_prime(x)
        answer += result
        
    return answer

# 입출력 예
# nums	        result
# [1,2,3,4]	    1
# [1,2,7,6,4]	4