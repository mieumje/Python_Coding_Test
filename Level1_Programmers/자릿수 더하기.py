def solution(n):
    answer = 0
    
    answer += n//100000000
    n = n % 100000000
    
    answer += n//10000000
    n = n % 10000000
    
    answer += n//1000000
    n = n % 1000000
    
    answer += n//100000
    n = n % 100000
    
    answer += n//10000
    n = n % 10000
    
    answer += n//1000
    n = n % 1000
    
    answer += n//100
    n = n % 100
    
    answer += n//10
    n = n % 10
    
    answer += n
    
    return answer

# N = 123
# answer = 0
# answer += N//100
# N = N % 100
# answer += N//10
# N = N % 10
# answer += N

# print(answer)

N = 123
print(solution(N))

N = 987
print(solution(N))