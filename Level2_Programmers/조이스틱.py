def solution(name):
    answer = 0
    tmp = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
           for char in name]
    answer = sum(tmp)
    min_move = len(name) - 1
    for i, _ in enumerate(name):
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
        min_move = min([min_move, i * 2 + len(name) - next, i + 2 * (len(name) - next)])
    answer += min_move
    return answer

# 입출력 예
# name	        return
# "JEROEN"	    56
# "JAN"	        23
# "ABABAAAAABA" 10

name = "JAN"
print(solution(name))
