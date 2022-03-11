def solution(n, m):
    answer = 0
    for _ in range(n):
        arr = list(map(int, input().split()))
        if len(arr) > m:
            return "error"
        min_value = min(arr)
        answer = max(answer, min_value)
    return answer


n, m = map(int, input().split())
print(solution(n, m))
