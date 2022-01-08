"""
채팅방에 누군가 들어오면 다음 메시지가 출력된다.
"[닉네임]님이 들어왔습니다."

채팅방에서 누군가 나가면 다음 메시지가 출력된다.
"[닉네임]님이 나갔습니다."

채팅방에서 닉네임을 변경하는 방법은 다음과 같이 두 가지이다.

채팅방을 나간 후, 새로운 닉네임으로 다시 들어간다.
채팅방에서 닉네임을 변경한다.
닉네임을 변경할 때는 기존에 채팅방에 출력되어 있던 메시지의 닉네임도 전부 변경된다.
"""

def solution(record):
    answer = []
    tmp = []                            # Enter, Leave 순서를 위한 arr
    users = {}
    messages = {
        "Enter" : "들어왔습니다.",
        "Leave" : "나갔습니다."
    }
    for i in record:
        a = i.split(" ")
        if(a[0] == "Enter"):            # 채팅방 입장
            users[a[1]] = a[2]          # users dictionary에 저장{uid : 닉네임}
            tmp.append([a[0], a[1]])    # Enter, 닉네임 입력
        elif(a[0] == "Change"):         # 닉네임 변경
            users[a[1]] = a[2]          # {uid : 닉네임} 업데이트
        else:                           # 채팅방 퇴장
            tmp.append([a[0], a[1]])    # Leave, 닉네임 입력
            
    # print(users, tmp)
    message = ""
    for i in tmp:                       # Enter, Leave 순서 확인
        message = f"{users[i[1]]}님이 {messages[i[0]]}" # 메세지
        answer.append(message)
    return answer

# 입출력 예
# record	
# ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# result
# ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

# 제한사항
# record는 다음과 같은 문자열이 담긴 배열이며, 길이는 1 이상 100,000 이하이다.
# 다음은 record에 담긴 문자열에 대한 설명이다.
    # 모든 유저는 [유저 아이디]로 구분한다.
    # [유저 아이디] 사용자가 [닉네임]으로 채팅방에 입장 - "Enter [유저 아이디] [닉네임]" (ex. "Enter uid1234 Muzi")
    # [유저 아이디] 사용자가 채팅방에서 퇴장 - "Leave [유저 아이디]" (ex. "Leave uid1234")
    # [유저 아이디] 사용자가 닉네임을 [닉네임]으로 변경 - "Change [유저 아이디] [닉네임]" (ex. "Change uid1234 Muzi")
    # 첫 단어는 Enter, Leave, Change 중 하나이다.
    # 각 단어는 공백으로 구분되어 있으며, 알파벳 대문자, 소문자, 숫자로만 이루어져있다.
    # 유저 아이디와 닉네임은 알파벳 대문자, 소문자를 구별한다.
    # 유저 아이디와 닉네임의 길이는 1 이상 10 이하이다.
    # 채팅방에서 나간 유저가 닉네임을 변경하는 등 잘못 된 입력은 주어지지 않는다.

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))