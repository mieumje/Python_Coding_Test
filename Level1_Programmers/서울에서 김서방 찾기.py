def solution(seoul):
    answer = ''
    for i in range(0, len(seoul)):
        if(seoul[i] == "Kim"):
            answer = f'김서방은 {i}에 있다'
    return answer



seoul = ["Jane", "Kim"]
print(solution(seoul))