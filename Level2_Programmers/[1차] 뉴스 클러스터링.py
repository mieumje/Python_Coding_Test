import math
def make_multiset(s):
    tmp = []
    for i in range(0, len(s) - 1):
        tmp_element = s[i]+s[i+1]
        if tmp_element.isalpha():
            tmp.append(tmp_element.upper())
    return tmp

def solution(str1, str2):
    answer = 0
    J = 0
    
    # 문자열 str1, str2를 다중집합으로 만들기
    str1_multiset = make_multiset(str1)
    str2_multiset = make_multiset(str2)
    if not list(set(str1_multiset) & set(str2_multiset)): # str1과 str2의 교집합이 없는 경우 자카드 유사도는 1
        J = 1
    else:
        b = list(set(str1_multiset) & set(str2_multiset))
        str1_cnt, str2_cnt = 0, 0
        for i in b:
            str1_cnt += str1_multiset.count(i)
            str2_cnt += str2_multiset.count(i)
        intersection = min(str1_cnt,str2_cnt)
        if str1_cnt == str2_cnt:
            cnt = 0
            for i in str1_multiset:
                for j in str2_multiset:
                    if i == j:
                        cnt += 1
                        break
            union = len(str1_multiset) + len(str2_multiset) - cnt
        else:
            union = max(str1_cnt,str2_cnt)
        J = intersection / union
    answer = math.floor(J * 65536)
    return answer



# 출력 형식
# 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로, 
# 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

# 예제 입출력
# str1	    str2	    answer
# FRANCE	french	    16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	    43690
# E=M*C^2	e=m*c^2	    65536

str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
print(solution(str1,str2))