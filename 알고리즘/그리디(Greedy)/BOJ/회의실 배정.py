def solution(times):
    answer = 0
    end_time = 0

    times.sort(key=lambda x: (x[1], x[0]))

    for start, end in times:
        if(start >= end_time):
            answer += 1
            end_time = end

    return answer


N = int(input())
times = []
for _ in range(N):
    start, end = map(int, input().split())
    times.append([start, end])

print(solution(times))
