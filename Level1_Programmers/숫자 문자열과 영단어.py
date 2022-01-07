"""
다음은 숫자의 일부 자릿수를 영단어로 바꾸는 예시입니다.
1478 → "one4seveneight"
234567 → "23four5six7"
10203 → "1zerotwozero3"

이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 
혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. 
s가 의미하는 원래 숫자를 return
"""
def solution(s):
    answer = ""
    words = {               # 숫자	영단어
        "zero" : "0",       # 0	    zero
        "one" : "1",        # 1	    one
        "two" : "2",        # 2	    two
        "three" : "3",      # 3	    three
        "four" : "4",       # 4	    four
        "five" : "5",       # 5	    five
        "six" : "6",        # 6	    six
        "seven" : "7",      # 7	    seven
        "eight" : "8",      # 8	    eight
        "nine" : "9",       # 9	    nine
    }
    tmp = ""
    for i in s:
        if i.isdigit():
            answer += i
            continue
        tmp += i
        if tmp in words:
            answer += words[tmp]
            tmp = ""
    return int(answer)

# 제한사항
# 1 ≤ s의 길이 ≤ 50
# s가 "zero" 또는 "0"으로 시작하는 경우는 주어지지 않습니다.
# return 값이 1 이상 2,000,000,000 이하의 정수가 되는 올바른 입력만 s로 주어집니다.

# 입출력 예
# s	                    result
# "one4seveneight"	    1478
# "23four5six7"	        234567
# "2three45sixseven"	234567
# "123"	                123
s = "one4seveneight"
print(solution(s))