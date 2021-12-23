def solution(a, b):
    answer = 0
    
    if a < b:
        for i in range(a, b+1):
            answer += i
    else:
        for i in range(b, a+1):
            answer += i
    return answer

a=5
b=3
print(solution(a,b))