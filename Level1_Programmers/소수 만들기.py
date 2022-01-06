"""
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, 
nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return
"""
from itertools import combinations
import math
def is_prime(num):
    check_prime = True
    N = int(math.sqrt(num))
    
    for i in range(2,N+1):
        if(num % i == 0):
            check_prime = False
            return False
    return check_prime

def solution(nums):
    answer = 0
    tmp_list = list(combinations(nums,3))
    tmp_sum = 0
    for i in range(0, len(tmp_list)):
        tmp_sum = tmp_list[i][0] + tmp_list[i][1] + tmp_list[i][2]
        if(is_prime(tmp_sum)) : answer += 1
        
    return answer

# 입출력 예
# nums	        result
# [1,2,3,4]	    1
# [1,2,7,6,4]	4

nums = [1,2,3,4]
print(solution(nums))