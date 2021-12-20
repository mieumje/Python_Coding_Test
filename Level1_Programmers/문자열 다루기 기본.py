## 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요. 
## 예를 들어 s가 "a234"이면 False를 리턴하고 "1234"라면 True를 리턴하면 됩니다.

def checkLength(s):
    if(len(s) == 4 or len(s) == 6):
        return True
def checkChar(s):
    if(s.isdigit()):
        return True

def solution(s):
    answer = True
    if(not checkLength(s)):
        return False
    if(not checkChar(s)):
        return False
    
    return answer


s = "12345"
print(solution(s))