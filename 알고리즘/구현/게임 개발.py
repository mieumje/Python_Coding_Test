""" 방향
    - 0 : 북쪽
    - 1 : 동쪽
    - 2 : 남쪽
    - 3 : 서쪽
    """


def solution():
    answer = 1  # 맵을 움직이며 방문한 칸의 수
    cnt = 0  # 회전 횟수

    N, M = map(int, input().split())  # 맵 크기 N * M
    # (x, y) = 현재 위치, Direction = 바라보는 방향
    x, y, Direction = map(int, input().split())

    arr = []    # 맵 정보, 0 = 육지, 1 = 바다
    for _ in range(N):
        arr.append(list(map(int, input().split())))

    def turn_left(Direction):   # 캐릭터 회전 (왼쪽으로 회전)
        Direction -= 1
        if Direction == -1:
            Direction = 3
        return Direction

    dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
    dy = [0, 1, 0, -1]  # 북, 동, 남, 서

    tmp = [[0] * M for _ in range(N)]  # 캐릭터가 방문한 배열 생성
    tmp[x][y] = 1   # 현재 위치 방문 체크

    while True:
        Direction = turn_left(Direction)
        nx = x + dx[Direction]
        ny = y + dy[Direction]

        if tmp[nx][ny] == 0 and arr[nx][ny] == 0:   # 회전한 후 방문하지 않은 곳 and 육지인 경우
            x, y = nx, ny
            tmp[x][y] = 1
            answer += 1
            cnt = 0
            continue
        else:   # 방문 했던 곳 or 바다인 경우 다시 회전
            cnt += 1

        if cnt == 4:    # 4방향 모두 갈 수 없는 경우
            nx = x - dx[Direction]
            ny = y - dy[Direction]

            if arr[nx][ny] == 0:    # 뒤로 갈 수 있는 경우 한 칸 뒤로 이동
                x, y = nx, ny
            else:   # 뒤 쪽 방향이 바다인 경우 종료
                break
            cnt = 0
    return answer


print(solution())
