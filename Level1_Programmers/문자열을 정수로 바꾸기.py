s = "1234"

def solution(s):
    answer = 0
    tmp = ''
    if(s.startswith('-')):
        for i in range(1,len(s)):
            tmp += s[i]
        answer = -int(tmp)
    else:
        answer = int(s)
    return answer

print(solution(s))