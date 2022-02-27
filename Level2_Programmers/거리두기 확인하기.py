#from queue import Queue
from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(row, col, place):
    visited = [[False for _ in range(5)] for _ in range(5)]
    # q = Queue()
    q = deque()
    visited[row][col] = 1
    # q.put((row, col, 0))
    q.append((row, col, 0))
    while len(q) > 0:
        cur = q.popleft()
        cur_x = cur[0]
        cur_y = cur[1]
        dist = cur[2]

        if dist > 2:
            continue
        if dist != 0 and place[cur_x][cur_y] == 'P':
            return False

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if nx < 0 or nx > 4 or ny < 0 or ny > 4:
                continue
            if visited[nx][ny] == True:
                continue
            if place[nx][ny] == 'X':
                continue

            visited[nx][ny] = True
            q.append((nx, ny, dist + 1))

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
# q = deque()
# print(len(q))
# q.append((1, 2, 3))
# print(q, len(q))
# q.append((0, 4, 2))
# print(q, len(q))
# x = q.popleft()
# print(x[0], x[2])
# print(q, len(q))
# q.popleft()
# print(q, len(q))
