def solution(N):
    answer = 0
    for Hour in range(N+1):             # 0시 ~ N시
        for Minute in range(60):        # 0분 ~ 59분
            for Second in range(60):    # 0초 ~ 59초
                # HH:MM:SS 형태로 문자열 생성
                tmp = f"{str(Hour)}:{str(Minute)}:{str(Second)}"
                if "3" in tmp:  # tmp 문자열에 "3"이 포함된 경우 answer 증가
                    answer += 1
    return answer


N = int(input())
print(solution(N))
