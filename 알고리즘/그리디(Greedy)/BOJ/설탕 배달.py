N = int(input())
answer = 0

while N >= 0:
    if N % 5 == 0:
        answer += N // 5
        break
    N -= 3
    answer += 1
    #print(N, answer)
#print(N, answer)
print(answer if N >= 0 else -1)
