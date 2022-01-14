""" 
프린터는 아래와 같은 방식으로 인쇄 작업을 수행합니다.

1. 인쇄 대기목록의 가장 앞에 있는 문서(J)를 대기목록에서 꺼냅니다.
2. 나머지 인쇄 대기목록에서 J보다 중요도가 높은 문서가 한 개라도 존재하면 J를 대기목록의 가장 마지막에 넣습니다.
3. 그렇지 않으면 J를 인쇄합니다.

예를 들어, 4개의 문서(A, B, C, D)가 순서대로 인쇄 대기목록에 있고 중요도가 2 1 3 2 라면 C D A B 순으로 인쇄하게 됩니다.

현재 대기목록에 있는 문서의 중요도가 순서대로 담긴 배열 priorities와 
내가 인쇄를 요청한 문서가 현재 대기목록의 어떤 위치에 있는지를 알려주는 location이 매개변수로 주어질 때, 
내가 인쇄를 요청한 문서가 몇 번째로 인쇄되는지 return
"""

def solution(priorities, location):
    answer = 0
    l = len(priorities)
    
    while(priorities):
        if(location == 0):                              # 요청한 문서가 첫 번째 대기목록에 위치할 때
            if(priorities[0] < max(priorities)):        # 요청한 문서보다 더 높은 우선순위의 문서가 존재하는 경우
                priorities.append(priorities.pop(0))    # 첫 번째 문서를 마지막 대기목록에 추가
                location = l - 1                        # 요청한 문서의 location은 마지막
            else:                                       # 요청한 문서의 우선순위가 가장 높을 때
                return answer + 1                       # return answer + 1
        else:                                           # 요청한 문서의 위치가 첫 번째가 아닐 경우
            if(priorities[0] < max(priorities)):        # 첫 번째 문서보다 더 높은 우선순위의 문서가 존재하는 경우
                priorities.append(priorities.pop(0))    # 첫 번째 문서를 마지막 대기목록에 추가
                location -= 1                           # 요청한 문서의 location은 -1(앞으로 한칸 땡겨짐)
            else:                                       # 첫 번째 문서의 우선순위가 가장 높은 경우
                priorities.pop(0)                       # 해당 문서를 대기목록에서 삭제
                location -= 1                           # 요청한 문서의 location은 -1
                answer += 1                             # answer += 1

# 입출력 예
# priorities	        location	return
# [2, 1, 3, 2]	        2	        1
# [1, 1, 9, 1, 1, 1]	0	        5
priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))