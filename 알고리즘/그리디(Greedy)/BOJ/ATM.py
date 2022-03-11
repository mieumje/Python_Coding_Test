def solution(N, P):
    answer = 0
    P.sort()
    tmp = 0
    for x in P:
        tmp += x
        answer += tmp
    return answer


N = int(input())
P = list(map(int, input().split()))

print(solution(N, P))
