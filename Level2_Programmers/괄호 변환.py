def check_correction(p):
    tmp = p.split("()")
    s = ""
    for i in tmp:
        s += "".join(i)
    if(s == "()"):
        return True
    else:
        return False
    
def solution(p):
    answer = ''
    if p == "":
        return ""
    if check_correction(p):
        return p
    else:
        tmp = p.split("()")
        for i in tmp:
            if i:
                l = len(i)
                for i in range(0, l):
                    if(i < l // 2):
                        answer += "("
                    else:
                        answer += ")"
            else:
                answer += "()"
        return answer


p = "()))((()"
print(solution(p))

