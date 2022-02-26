from queue import Queue

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col, place):
    visited = [[False for _ in range(5)] for _ in range(5)]
    q = Queue()
    visited[row][col] = 1
    q.put((row, col, 0))

    while q:
        cur = q.get()
        cur_x = cur[0]
        cur_y = cur[1]

        if cur[2] > 2:
            continue
        if cur[2] != 0 and place[cur_x][cur_y] == 'P':
            return False

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if visited[nx][ny]:
                continue
            if place[nx][ny] == 'X':
                continue

            visited[nx][ny] = 1
            q.put((nx, ny, cur[2] + 1))
    return True


def check_distance(place):
    for row in range(5):
        for col in range(5):
            if place[row][col] == 'P':
                if bfs(row, col, place) == False:
                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        if check_distance(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer

# 입출력 예
# places	                                        result
# [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
#  ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
#  ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
#  ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
#  ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	[1, 0, 1, 1, 1]


places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))
