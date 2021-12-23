def solution(n):
    answer = ''
    if(n == 1) : answer += '수'
    if(n == 2) : answer += '수박'
    
    if(n % 2 == 1):
        answer = '수박' * (n//2)
        answer += '수'
    else:
        answer = '수박' * (n//2)
    return answer

n = 4
print(solution(n))
