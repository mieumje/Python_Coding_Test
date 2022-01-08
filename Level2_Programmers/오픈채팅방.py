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

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))