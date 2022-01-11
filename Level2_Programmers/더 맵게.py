"""
매운 것을 좋아하는 Leo는 모든 음식의 스코빌 지수를 K 이상으로 만들고 싶습니다. 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 Leo는 스코빌 지수가 가장 낮은 두 개의 음식을 아래와 같이 특별한 방법으로 섞어 새로운 음식을 만듭니다.

섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

Leo는 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복하여 섞습니다.
Leo가 가진 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때, 
모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return.

"""
import heapq
def solution(scoville, K):
    answer = 0
                                                    # 남은 음식이 1개라면 새로운 스코빌 지수를 만들 수 없음
    while len(scoville) > 1 and scoville[0] < K:    # 길이가 1이거나, 제일 작은 스코빌 지수가 K를 넘으면 종료
        first_scoville, second_scoville = heapq.heappop(scoville), heapq.heappop(scoville)  # 가장 맵지 않은 음식, 두 번째로 맵지 않은 음식의 스코빌 지수
        new_scoville = first_scoville + (second_scoville * 2)   # 섞은 음식의 스코빌 지수
        heapq.heappush(scoville, new_scoville)                  # 섞은 음식의 스코빌 지수를 push
        answer += 1                                             # cnt += 1
    
    if scoville[0] < K: #모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1
        return -1
    return answer

# 입출력 예
# scoville	            K	return
# [1, 2, 3, 9, 10, 12]	7	2
# [1, 2, 3, 9, 10, 12]  106 -1
scoville = [1, 2, 3, 9, 10, 12]
K = 106
print(solution(scoville,K))