import re

def step_1(x): # 대문자 > 소문자 치환
    str = ''
    for i in x:
        if i.isupper:
            i = i.lower()
        str += i
    return str

def step_2(x): # 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거
    # char = "!@#*"
    # for i in range(len(char)):
    #   x = x.replace(char[i], "")
    # str = x
    str = ''
    str = re.sub('[^a-z0-9\-_.]', '', x)
    return str

def step_3(x): # 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    cnt = 0
    str = ''

    for i in range(len(x)):
        plus = ""
        if x[i] == ".":
            cnt += 1
            plus = x[i]
            if cnt > 1:
                plus = ""
        else:
            cnt = 0
            plus = x[i]
        str += plus
    return str

def step_4(x): # 마침표(.)가 처음이나 끝에 위치하면 제거
    str = ''
    if x.startswith("."):
        str = x[1:]
    else:
        str = x
    if str.endswith("."):
        str = str[0:-1]
    else:
        str = str  
    return str

def step_5(x): # 빈 문자열이라면, "a"를 대입
    str = ""
    if x == "":
        x += "a"
    str = x
    return str  

def step_6(x): # 길이가 16자 이상이면, 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    str = ""
    if len(x) >= 16:
        str = x[0:15]
    else:
        str = x
    while(True): # 제거 후, 마침표(.)가 끝에 위치하면 끝에 위치한 마침표(.)를 제거
        if str.endswith("."):
            str = str[0:-1]
        else:
            break
    return str

def step_7(x): # 길이가 2자 이하라면 길이가 3이 될 때까지 마지막 문자를 반복해 끝에 붙인다
    str = ''
    while(True):
        if len(x) <= 2:
            x += x[-1]
        else:
            break
    str = x
    return str
    
def solution(new_id):
    #answer = step_7(step_6(step_5(step_4(step_3(step_2(step_1(new_id)))))))
      
    answer = step_1(new_id) # 1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
    answer = step_2(answer) # 2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
    answer = step_3(answer) # 3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
    answer = step_4(answer) # 4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
    answer = step_5(answer) # 5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
    answer = step_6(answer) # 6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    answer = step_7(answer) # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.

    return answer

# [제한사항]
# new_id는 길이 1 이상 1,000 이하인 문자열입니다.
# new_id는 알파벳 대문자, 알파벳 소문자, 숫자, 특수문자로 구성되어 있습니다.
# new_id에 나타날 수 있는 특수문자는 -_.~!@#$%^&*()=+[{]}:?,<>/ 로 한정됩니다.

# [입출력 예]
# no	new_id	                        result
# 예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
# 예2	"z-+.^."	                    "z--"
# 예3	"=.="	                        "aaa"
# 예4	"123_.def"	                    "123_.def"
# 예5	"abcdefghijklmn.p"	            "abcdefghijklmn"

new_id = "...!@BaT#*..y.abcdefghijklm"
print(solution(new_id))

# 입출력 예 #1
# 1단계 대문자 'B'와 'T'가 소문자 'b'와 't'로 바뀌었습니다.
# "...!@BaT#*..y.abcdefghijklm" → "...!@bat#*..y.abcdefghijklm"

# 2단계 '!', '@', '#', '*' 문자가 제거되었습니다.
# "...!@bat#*..y.abcdefghijklm" → "...bat..y.abcdefghijklm"

# 3단계 '...'와 '..' 가 '.'로 바뀌었습니다.
# "...bat..y.abcdefghijklm" → ".bat.y.abcdefghijklm"

# 4단계 아이디의 처음에 위치한 '.'가 제거되었습니다.
# ".bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

# 5단계 아이디가 빈 문자열이 아니므로 변화가 없습니다.
# "bat.y.abcdefghijklm" → "bat.y.abcdefghijklm"

# 6단계 아이디의 길이가 16자 이상이므로, 처음 15자를 제외한 나머지 문자들이 제거되었습니다.
# "bat.y.abcdefghijklm" → "bat.y.abcdefghi"

# 7단계 아이디의 길이가 2자 이하가 아니므로 변화가 없습니다.
# "bat.y.abcdefghi" → "bat.y.abcdefghi"

# 따라서 신규 유저가 입력한 new_id가 "...!@BaT#*..y.abcdefghijklm"일 때, 네오의 프로그램이 추천하는 새로운 아이디는 "bat.y.abcdefghi" 입니다.