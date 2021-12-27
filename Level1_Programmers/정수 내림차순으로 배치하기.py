def solution(n):
    answer = 0
    tmpN = str(n)
    tmpArr = []
    
    for i in tmpN:
        tmpArr.append(i)

    tmpArr.sort(reverse=True)
    tmpStr = ''
    
    for i in tmpArr:
        tmpStr += i
    answer = int(tmpStr)
    
    return answer

n = 118372
print(solution(n))