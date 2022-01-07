def ratings(cnt):
    if cnt < 2 : return 6   # 순위 : 6, 그외(1, 0개)
    elif cnt < 3 : return 5 # 순위 : 5, 2개 번호가 일치
    elif cnt < 4 : return 4 # 순위 : 4, 3개 번호가 일치
    elif cnt < 5 : return 3 # 순위 : 3, 4개 번호가 일치
    elif cnt < 6 : return 2 # 순위 : 2, 5개 번호가 일치
    else: return 1          # 순위 : 1, 6개 번호가 모두 일치
    
def solution(lottos, win_nums):
    low_cnt = 0
    high_cnt = 0
    for i in lottos:
        if i in win_nums:
            low_cnt += 1
            high_cnt += 1
        if i == 0:
            high_cnt += 1
            
    high_rating, low_rating = ratings(high_cnt), ratings(low_cnt) 
    return [high_rating, low_rating]

# 입출력 예
# lottos	            win_nums	                result
# [44, 1, 0, 0, 31, 25]	[31, 10, 45, 1, 6, 19]	    [3, 5]
# [0, 0, 0, 0, 0, 0]	[38, 19, 20, 40, 15, 25]	[1, 6]
# [45, 4, 35, 20, 3, 9]	[20, 9, 3, 45, 4, 35]	    [1, 1]
lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos,win_nums))