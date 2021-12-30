#array의 각 element 중 divisor로 나누어 떨어지는 값을 오름차순으로 정렬한 배열을 반환
#divisor로 나누어 떨어지는 element가 하나도 없다면 배열에 -1을 담아 반환

# arr	        divisor	    return
# [5, 9, 7, 10]	5	        [5, 10]
# [2, 36, 1, 3]	1	        [1, 2, 3, 36]
# [3,2,6]	    10	        [-1]

def solution(arr, divisor):
    answer = []
    
    if divisor == 1: # 1로 나누면 모두 나누어 떨어짐
        answer = sorted(arr)
        return answer
    
    for i in arr:
        if i % divisor == 0 :
            answer.append(i)
    
    if len(answer) == 0: # divisor로 나누어 떨어지는 원소가 없으면 -1을 담아 반환
        answer.append(-1)
        return answer
    
    answer = sorted(answer) # 오름차순으로 정렬
    
    return answer

print(solution([5, 9, 7, 10],5))