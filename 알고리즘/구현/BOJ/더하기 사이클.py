N = int(input())


def solution(N):
    answer = 0
    tmp = N
    while True:
        tmp = int(str(tmp % 10) + str((tmp//10) + (tmp % 10))[-1])
        answer += 1
        if tmp == N:
            break
    return answer


print(solution(N))
