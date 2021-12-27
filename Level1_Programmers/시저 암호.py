startPointUpperCase = 64 # A = 65 ~ Z = 90
startPointLowerCase = 96 # a = 97 ~ z = 122
endPointUpperCase = 90
endPointLowerCase = 122

def asciiToChrLowerCase(i,n):
    tmpASCII = ord(i)
    if(tmpASCII + n > endPointLowerCase):
        tmpChr = chr(startPointLowerCase + n - (endPointLowerCase - ord(i)))
    else:
        tmpChr = chr(tmpASCII + n)
    return tmpChr

def asciiToChrUpperCase(i,n):
    tmpASCII = ord(i)
    if(tmpASCII + n > endPointUpperCase):
        tmpChr = chr(startPointUpperCase + n - (endPointUpperCase - ord(i)))
    else:
        tmpChr = chr(tmpASCII + n)
    return tmpChr

def solution(s, n):
    answer = ''
    for i in s:
        if(i == " "):
            answer += " "
        if(i.isupper()):
            answer += asciiToChrUpperCase(i,n)
        if(i.islower()):
            answer += asciiToChrLowerCase(i,n)
    return answer

s = "bC"
n = 25
print(solution(s, n))    

s = "AaZz"
n = 25
print(solution(s, n))    

