def solution(n):
    answer = []
    tmpStr = str(n)
    for i in tmpStr:
        answer.append(int(i))
    answer.reverse()
    return answer

n = 12345
print(solution(n))