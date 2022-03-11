def solution(N, P):
    answer = 0
    P.sort()
    tmp = []
    for i in range(0, N):
        time = 0
        for j in range(0, i + 1):
            time += P[j]
        tmp.append(time)

    answer = sum(tmp)
    return answer


N = int(input())
P = list(map(int, input().split()))

print(solution(N, P))
