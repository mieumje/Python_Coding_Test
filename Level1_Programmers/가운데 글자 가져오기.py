def solution(s):
    answer = ''
    l = len(s)
    x = l // 2
    if l % 2 == 0:
        return s[x-1] + s[x]
    else:
        return s[x]
    
# s	        return
# "abcde"	"c"
# "qwer"	"we"
s = "abcde"
print(solution(s))