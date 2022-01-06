"""
제한사항
absolutes의 길이는 1 이상 1,000 이하입니다.
absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
signs의 길이는 absolutes의 길이와 같습니다.
signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.
"""

def solution(absolutes, signs):
    answer = 0
    length = len(absolutes)
    
    for i in range(0, length):
        if(signs[i] == True):
            answer += absolutes[i]
        else:
            answer += absolutes[i] * -1
    
    return answer

# 입출력 예
# absolutes	signs	            result
# [4,7,12]	[True,False,True]	9
# [1,2,3]	[False,False,True]	0

absolutes = [1,2,3]
signs = [False,False,True]

print(solution(absolutes, signs))