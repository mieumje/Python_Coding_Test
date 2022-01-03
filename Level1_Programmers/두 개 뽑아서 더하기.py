# numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return
from itertools import combinations

def solution(numbers):
    answer = []
    combs = {}
    tmp = list(combinations(numbers, 2)) # numbers에서 2개로 조합할 수 있는 모든 경우의 수
    
    for i in tmp:
        sum = i[0] + i[1] # 조합의 합
        combs[sum] = 1 # 조합의 합으로 나올 수 있는 경우가 두 개 이상인 경우 하나만 취급
    
    for i in combs:
        answer.append(i)
    
    return sorted(answer)

# 입출력 예
# numbers	    result
# [2,1,3,4,1]	[2,3,4,5,6,7]
# [5,0,2,7]	    [2,5,7,9,12]

numbers = [5,0,2,7]
print(solution(numbers))

"""

입출력 예 #1

2 = 1 + 1 입니다. (1이 numbers에 두 개 있습니다.)
3 = 2 + 1 입니다.
4 = 1 + 3 입니다.
5 = 1 + 4 = 2 + 3 입니다.
6 = 2 + 4 입니다.
7 = 3 + 4 입니다.
따라서 [2,3,4,5,6,7] 을 return 해야 합니다.

입출력 예 #2

2 = 0 + 2 입니다.
5 = 5 + 0 입니다.
7 = 0 + 7 = 5 + 2 입니다.
9 = 2 + 7 입니다.
12 = 5 + 7 입니다.
따라서 [2,5,7,9,12] 를 return 해야 합니다.

"""