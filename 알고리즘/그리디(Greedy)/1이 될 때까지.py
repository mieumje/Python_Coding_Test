def solution(n, k):
    answer = 0
    while True:
        if n == 1:
            break

        if n % k == 0:
            n = n // k
            answer += 1
        else:
            n = n - 1
            answer += 1
    return answer


n, k = map(int, input().split())

print(solution(n, k))
