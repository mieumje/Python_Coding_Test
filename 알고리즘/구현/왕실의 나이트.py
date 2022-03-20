def solution(input):
    answer = 0

    # a ~ h = 97 ~ 104
    x, y = ord(input[0]) - 96, int(input[1])        # 현재 나이트의 좌표
    moves = [(-1, 2), (1, 2), (2, 1), (2, -1),
             (1, -2), (-1, -2), (-2, -1), (-2, 1)]  # 나이트가 움직일 수 있는 방향

    for move in moves:
        nx = x + move[0]
        ny = y + move[1]
        if nx > 8 or ny > 8 or nx < 1 or ny < 1:    # 8 * 8 체스판을 넘어간 경우는 정답 X
            continue
        answer += 1
    return answer


input = input()
print(solution(input))
