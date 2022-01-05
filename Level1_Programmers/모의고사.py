# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...
''' 
1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return
'''
def solution(answers):
    arr1 = [1, 2, 3, 4, 5]                  # 수포자 1
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]         # 수포자 2
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]   # 수포자 3
    
    answer_cnt = [0,0,0]                    # [수포자 1 정답 수, 수포자 2 정답 수, 수포자 3 정답 수]
    answer = []
    
    for i in range(0, len(answers)):
        if answers[i] == arr1[i % len(arr1)]:
            answer_cnt[0] += 1
        if answers[i] == arr2[i % len(arr2)]:
            answer_cnt[1] += 1
        if answers[i] == arr3[i % len(arr3)]:
            answer_cnt[2] += 1

    for i in range(0, len(answer_cnt)):
        if answer_cnt[i] == max(answer_cnt):
            answer.append(i+1)

    return answer

# 입출력 예
# answers	    return
# [1,2,3,4,5]	[1]
# [1,3,2,4,2]	[1,2,3]

answers = [1,3,2,4,2]
print(solution(answers))