from numpy import math


def solution(n, times):
    def accumulate(mid, times):
        tmp = 0
        for time in times:
            tmp += mid // time
        return tmp

    answer = 0
    times.sort()

    left = 1
    right = times[-1] * n

    while left < right:
        mid = math.trunc((left + right) / 2)

        sum = accumulate(mid, times)
        print(left, mid, right, sum)
        if sum > n:
            right = mid - 1
        else:
            left = mid + 1
    
    return mid


# 입출력 예
# n	        times	    return
# 6	        [7, 10]	    28

n = 6
times = [7, 10]
print(solution(n, times))
