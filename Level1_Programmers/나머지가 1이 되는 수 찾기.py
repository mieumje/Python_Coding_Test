def solution(n):
    answer = 1
    while(True):
        if n % answer == 1:
            return answer
        else:
            answer += 1
            
# 제한사항
# 3 ≤ n ≤ 1,000,000

# 입출력 예
# n	    result
# 10	3
# 12	11