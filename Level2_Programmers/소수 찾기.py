"""
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 
"""
from itertools import permutations
import math
def is_prime(nums):
    if nums == 0 or nums == 1:  # 입력된 숫자가 0 혹은 1일 경우 소수가 아님으로 return
        return
    else:
        for i in range(2, int(math.sqrt(nums) + 1)):    # 2부터 입력된 숫자의 제곱근 + 1만큼 반복하면서 나누어 떨어지는지 판별
            if nums % i == 0:                           # 나누어 떨어지면 소수가 아님
                return
    return True                 # 소수일 경우 return True

def solution(numbers):
    answer = 0
    number = []
    tmp = []
    
    for i in numbers:   # 문자열 numbers의 한자리 숫자를 number 리스트에 push
        number.append(i)
    
    for i in range(1,len(number)+1):    # number에 있는 한자리 숫자로 만들 수 있는 숫자의 종류
        permute = list(permutations(number,i))
        for j in permute:               # 한자리 수부터 len(number)만큼의 조합의 수
            tmp.append(int(''.join(j))) # 생성된 숫자를 tmp 리스트에 push
    number_permutation = list(set(tmp)) # tmp 리스트에서 중복 제거
    
    for i in number_permutation:        # 중복이 제거된 숫자의 조합에서 소수인지 아닌지 판별
        if(is_prime(i)):                # 소수라면 answer += 1
            answer += 1
            
    return answer
# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

# 입출력 예
# numbers	return
# "17"	    3
# "011"	    2

# 입출력 예 설명
# 예제 #1
# [1, 7]으로는 소수 [7, 17, 71]를 만들 수 있습니다.

# 예제 #2
# [0, 1, 1]으로는 소수 [11, 101]를 만들 수 있습니다.

# 11과 011은 같은 숫자로 취급합니다.

numbers = "011"
print(solution(numbers))
