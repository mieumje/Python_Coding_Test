# 배열 arr = 0 ~ 9 숫자로 이루어 짐
# 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거

def solution(arr):
    answer = []
    tmp = arr[0]
    answer.append(tmp)
    
    for i in arr:
        if i != tmp:
            tmp = i
            answer.append(i)
    
    return answer

# arr	            answer
# [1,1,3,3,0,1,1]	[1,3,0,1]
# [4,4,4,3,3]	    [4,3]

print(solution([1,1,3,3,0,1,1]))