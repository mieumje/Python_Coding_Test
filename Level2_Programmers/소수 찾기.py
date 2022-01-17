"""
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.
각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 
"""
import math
from itertools import permutations

def solution(numbers):
    
    answer = 0
    
    a = []
    
    for i in numbers:
        a.append(i)
    
    p = []
    
    for i in range(1,len(numbers)+1):
        permute = list(permutations(a,i))
        for j in range(0,len(permute)):
            p.append(int(''.join(permute[j])))
    
    arr = list(set(p))
    
    for i in range(0,len(arr)):
        flag = 0
        if arr[i] == 0 or arr[i] == 1:
            continue
        else:
            for j in range(2,int(math.sqrt(arr[i]) + 1)):
                if arr[i] % j == 0:
                    flag = 1
            if flag == 0:
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
