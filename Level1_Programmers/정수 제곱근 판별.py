import math
def solution(n):
    answer = 0
    tmp = math.sqrt(n)
    if(tmp % 1 == 0.0):
        tmp = int(tmp) + 1
        answer = int(math.pow(tmp,2))
        return answer
    else:
        return -1

n = 121 # 144
print(solution(n))
n = 3	# -1
print(solution(n))
