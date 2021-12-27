def solution(s):
    answer = ''
    tmpArr = s.split(" ")
    for i in tmpArr:
        for x in range(0,len(i)):
            if(x%2 == 0): answer += i[x].upper()
            else: answer += i[x]
        answer += " "
    answer = answer[:-1]
    return answer

s = "try hello world"
print(solution(s))
