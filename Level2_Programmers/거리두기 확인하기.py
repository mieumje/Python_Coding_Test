# p 기준 상하좌우 p의 개수 1 이상이면 0
# o 기준 상하좌우 p의 개수 2 이상이면 0

def solution(places):
    answer = []
    
    for i in places:
        arr = []
        for j in i:
            tmp = []
            for x in j:
                tmp.append(x)
            arr.append(tmp)

        for x in range(0, len(arr)):
            for y in range(0, len(arr[x])):
                check_distance = 1
                if y == 0:
                    left = ''
                else:
                    left = arr[x][y-1]
                if x == 4:
                    bottom = ''
                else:
                    bottom = arr[x+1][y]
                if x == 0:
                    top = ''
                else:
                    top = arr[x-1][y]
                if y == 4:
                    right = ''
                else:
                    right = arr[x][y+1]
                cur = arr[x][y]
                left_right_top_bottom = [left, right, top, bottom]
                cnt_p = left_right_top_bottom.count('P')
                
                if cur == 'P':
                    if cnt_p >= 1:
                        check_distance = 0
                        break
                if cur == 'O':
                    if cnt_p >= 2:
                        check_distance = 0
                        break
        answer.append(check_distance)
                
            
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
