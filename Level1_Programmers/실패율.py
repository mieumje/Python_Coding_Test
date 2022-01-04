# 실패율은 다음과 같이 정의한다.
# 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

# 전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
# 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return

def solution(N, stages):
    answer = []
    length = len(stages)
    stages_fail_ratings = {}
    
    for i in range(1, N+1):                         # 1단계 부터 N단계 까지
        cnt = stages.count(i)                       # i단계에 있는 플레이어 수 (i단계에 도달했지만 클러어 하지 못한 플레이어)
        if cnt == 0:                                # i단계를 클리어하지 못한 플레이어가 없을 때
            stages_fail_ratings[i] = 0              # 실패율은 0
        else:                                       # i단계를 클리어하지 못한 플레이어가 있을 때
            stages_fail_ratings[i] = cnt / length   # 실패율은 플레이어 수 / 스테이지에 도달한 플레이어 수
        length -= cnt                               # i단계의 실패율을 구한 후 다음 단계에 도달한 플레이어 수는 전체 플레이어 - i단계 플레이어
          
          # {단계 : 실패율}의 형태의 dict stage_fail_ratings를 실패율을 기준으로 내림차순으로 정렬
          # 실패율이 같은 경우, 작은 번호의 스테이지가 오도록 단계는 오름차순으로 정렬
    tmp = sorted(stages_fail_ratings.items(), key = lambda items : (-items[1], items[0]))
    
    for i in tmp:
        # answer 배열에 정렬된 스테이지를 넣음
        answer.append(i[0])
    
    return answer


# 제한사항
# 스테이지의 개수 N은 1 이상 500 이하의 자연수이다.
# stages의 길이는 1 이상 200,000 이하이다.
# stages에는 1 이상 N + 1 이하의 자연수가 담겨있다.
# 각 자연수는 사용자가 현재 도전 중인 스테이지의 번호를 나타낸다.
# 단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
# 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오도록 하면 된다.
# 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.

# 입출력 예
# N	    stages	                    result
# 5	    [2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
# 4	    [4,4,4,4,4]	                [4,1,2,3]
N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))