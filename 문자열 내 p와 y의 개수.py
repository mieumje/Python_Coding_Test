## 문자열 s
## s에 'p'의 개수와 'y'의 개수를 비교
## 같으면 True, 다르면 False를 return
## 'p', 'y' 모두 하나도 없는 경우는 항상 True를 return
## 개수를 비교할 때 대문자, 소문자는 구별하지 않음
## s = "pPooyY" -> True, s = "Pyy" -> False

def lowerString(s):
    lower_str = s.lower()
    return lower_str

def check_P_Y_InString(s):
    if('p' in s or 'y' in s):
        return True
def countP(s):
    cnt = 0
    for i in s:
        if(i == 'p'):
                cnt += 1
    return cnt

def countY(s):
    cnt = 0
    for i in s:
        if(i == 'y'):
                cnt += 1
    return cnt

def solution(s):
    tmpStr = lowerString(s)
    
    if(not check_P_Y_InString(tmpStr)):
        return True
    if(countP(tmpStr) == countY(tmpStr)):
        return True
    else:
        return False



##s = "pPooyY"
s = "Pyy"
print(solution(s))