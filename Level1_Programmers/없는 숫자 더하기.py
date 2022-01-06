def solution(numbers):
    arr = [0,0,0,0,0,0,0,0,0,0] # 0 ~ 9
    
    for i in numbers:
        arr[i] += 1
    
    sum = 0
    
    for i in range(0, len(arr)):
        if(arr[i] == 0):
            sum += i
    
    if(sum == 0):
        return -1
    else:
        return sum


# 제한사항
# 1 ≤ numbers의 길이 ≤ 9
# 0 ≤ numbers의 모든 수 ≤ 9
# numbers의 모든 수는 서로 다릅니다.

# 입출력 예
# numbers	        result
# [1,2,3,4,6,7,8,0]	14
# [5,8,4,0,6,7,9]	6

numbers = [5,8,4,0,6,7,9]
print(solution(numbers))