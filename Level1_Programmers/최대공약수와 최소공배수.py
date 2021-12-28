def solution(n, m):
    maxNum = max(n,m)
    LCM, GCD = 0, 0 #최소공배수, 최대공약수
    answer = []
    
    for i in range(1, maxNum+1):
        if(n % i == 0 and m % i == 0):
            GCD = i
    LCM = (n * m) // GCD    #최소공배수 = 두 자연수의 곱 / 최대공약수
    answer = [GCD, LCM]
    return answer

n, m = 3, 12
print(solution(n,m))

n, m = 1, 5
print(solution(n,m))