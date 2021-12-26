def solution(s, n):
    answer = ''
    for i in s:
        tmpASCII = ord(i)
        if(tmpASCII == 122):
            tmpASCII = 96
        if(tmpASCII == 90):
            tmpASCII = 64
        if(tmpASCII == 32):
            answer += " "
        else:
            tmpChr = chr(tmpASCII + n)
            answer += tmpChr
    return answer

s = "AB"
n = 1
print(solution(s, n))    

s = "z"
n = 1
print(solution(s, n))    

s = "a B z"
n = 4
print(solution(s, n))    

print(ord(" "))