# A = 65 ~ Z = 90
# a = 97 ~ z = 122

def solution(s, n):
    answer = ''
    for i in s:
        if(i == " "):
            answer += " "
        if(i.isupper()):
            #print(f"{i} is Upper")
            #print(ord(i) + n, ord(i), n - (90 - ord(i)))
            if((ord(i) + n) > 90):
                x = 64
                #print(chr(x + 26 - n))
                answer += chr(x + n - (90 - ord(i)))
            else:
                answer += chr(ord(i) + n)
        if(i.islower()):
            #print(f"{i} is Lower")
            #print(ord(i) + n)
            if((ord(i) + n) > 122):
                x = 96
                #print(chr(x + 26 - n))
                answer += chr(x + n - (122 - ord(i)))
            else:
                answer += chr(ord(i) + n)
    return answer

s = "bC"
n = 25
print(solution(s, n))    

s = "AaZz"
n = 25
print(solution(s, n))    

