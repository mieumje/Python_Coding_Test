def solution(progresses, speeds):
    answer = []
    cnt = 1
    speed = (100 - progresses[0]) // speeds[0]  # 첫번째 작업이 끝나는데 걸리는 일
    
    for i in range(1, len(progresses)):
        if (speed >= (100 - progresses[i]) // speeds[i]):   # 다음 작업 속도가 더 느릴 경우, 이전 작업이 완료되면 같이 완료
            cnt += 1
        else:
            answer.append(cnt)                              # 다음 작업 속도가 더 빠를 경우, 이전 작업 완료
            speed = (100 - progresses[i]) // speeds[i]      # 다음 작업 속도로 걸리는 일 초기화
            cnt = 1                                         # 완료 될 작업의 수 초기화
    answer.append(cnt)                                      # 마지막 완료된 작업 추가
    return answer


# 입출력 예
# progresses	            speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))