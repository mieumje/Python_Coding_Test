N = int(input())

for _ in range(N):
    tmp = input()
    answer = 0
    cnt = 0
    for x in tmp:
        if x == 'O':
            cnt += 1
            answer += cnt
        else:
            cnt = 0
    print(answer)
