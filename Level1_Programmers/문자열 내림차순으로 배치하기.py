## 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 return
## s는 영문 대소문자로 구성
## 대문자는 소문자보다 작은 것으로 간주

def solution(s):
    answer = ''
    tmp = sorted(s)
    answer = ''.join(reversed(tmp))
    
    return answer

s = "Zbcdefg"
print(solution(s))