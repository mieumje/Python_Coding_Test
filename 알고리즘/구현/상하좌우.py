def solution(N, moves):
    x, y = 1, 1         # 시작 위치
    dx = [0, 0, -1, 1]  # 좌, 우, 상, 하
    dy = [-1, 1, 0, 0]  # 좌, 우, 상, 하
    move_type = ['L', 'R', 'U', 'D']

    for move in moves:
        for j in range(4):
            if move == move_type[j]:
                nx = x + dx[j]
                ny = y + dy[j]
        if nx < 1 or ny < 1 or nx > N or ny > N:    # x,y 좌표가 N*N을 벗어난 경우
            continue
        x = nx
        y = ny
    return x, y


N = int(input())
moves = input().split()
x, y = solution(N, moves)


print(x, y)
