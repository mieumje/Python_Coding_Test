def solution(n, lost, reserve):    
    answer = n - len(lost)  # 수업을 들을 수 있는 학생 수 = 전체 학생 수 - 체육복이 없는 학생 수
    
    lost.sort()
    reserve.sort()
    
    for i in lost:          # 체육복이 없는 학생 중 여벌의 체육복이 있는 학생의 경우
        if i in reserve:
            lost.remove(i)
            reserve.remove(i)
            answer += 1
    
    for i in lost:          # 체육복이 없는 학생이 자신의 앞, 뒤 학생에게 체육복을 빌린 경우
        if i-1 in reserve:
            answer += 1
            reserve.remove(i-1)
            continue
        elif i+1 in reserve:
            answer += 1
            reserve.remove(i+1)
    
    return answer

# 입출력 예
# n	lost	reserve	    return
# 5	[2, 4]	[1, 3, 5]	5
# 5	[2, 4]	[3]	        4
# 3	[3]	    [1]	        2

n = 5
lost = [2,4]
reserve = [1,3,5]
print(solution(n,lost,reserve))