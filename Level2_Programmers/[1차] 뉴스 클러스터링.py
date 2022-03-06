from collections import Counter


def make_multiset(s):
    tmp = []
    for i in range(0, len(s) - 1):
        tmp_element = s[i]+s[i+1]
        if tmp_element.isalpha():
            tmp.append(tmp_element.upper())
    return tmp


def solution(str1, str2):
    # 문자열 str1, str2를 다중집합으로 만들기
    str1_multiset = make_multiset(str1)
    str2_multiset = make_multiset(str2)
    Counter1 = Counter(str1_multiset)
    Counter2 = Counter(str2_multiset)

    a = list((Counter1 & Counter2).elements())  # inter
    b = list((Counter1 | Counter2).elements())  # union

    if len(a) == 0 and len(b) == 0:
        return 65536
    else:
        return int((len(a) / len(b)) * 65536)


# 출력 형식
# 입력으로 들어온 두 문자열의 자카드 유사도를 출력한다. 유사도 값은 0에서 1 사이의 실수이므로,
# 이를 다루기 쉽도록 65536을 곱한 후에 소수점 아래를 버리고 정수부만 출력한다.

# 예제 입출력
# str1	    str2	    answer
# FRANCE	french	    16384
# handshake	shake hands	65536
# aa1+aa2	AAAA12	    43690
# E=M*C^2	e=m*c^2	    65536
str1 = 'FRANCE'
str2 = 'french'
print(solution(str1, str2))
str1 = 'handshake'
str2 = 'shake hands'
print(solution(str1, str2))
str1 = 'aa1+aa2'
str2 = 'AAAA12'
print(solution(str1, str2))
str1 = 'E=M*C^2'
str2 = 'e=m*c^2'
print(solution(str1, str2))
print((0/3)*65536)
