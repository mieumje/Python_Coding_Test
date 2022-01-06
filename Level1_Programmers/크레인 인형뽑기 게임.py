"""
게임 화면의 격자의 상태가 담긴 2차원 배열 board와 인형을 집기 위해 크레인을 작동시킨 위치가 담긴 배열 moves가 매개변수로 주어질 때, 
크레인을 모두 작동시킨 후 터트려져 사라진 인형의 개수를 return

크레인 작동 시 인형이 집어지지 않는 경우는 없으나 만약 인형이 없는 곳에서 크레인을 작동시키는 경우에는 아무런 일도 일어나지 않습니다.
또한 바구니는 모든 인형이 들어갈 수 있을 만큼 충분히 크다고 가정합니다.

게임 사용자는 크레인을 좌우로 움직여서 멈춘 위치에서 가장 위에 있는 인형을 집어 올릴 수 있습니다. 
집어 올린 인형은 바구니에 쌓이게 되는 데, 이때 바구니의 가장 아래 칸부터 인형이 순서대로 쌓이게 됩니다.
만약 같은 모양의 인형 두 개가 바구니에 연속해서 쌓이게 되면 두 인형은 터뜨려지면서 바구니에서 사라지게 됩니다. 
"""

def remove_basket_item(basket):
    first_itme, second_item = basket[-1], basket[-2] # basket에 담긴 맨 위쪽의 인형 2개
    if(first_itme == second_item):                   # 상위 두 개 인형이 같은 인형이면
        basket.pop(-1)                               # basket에서 인형 2개를 제거
        basket.pop(-1)                               
        return 2                                     # 점수 2점 추가
    else: return 0

def solution(board, moves):
    answer = 0
    basket = []                         # 집은 인형을 담을 배열
    for i in moves:                     # 크레인이 움직일 위치
        move = i - 1                    # 배열의 index는 0부터 시작이라 -1
        for j in board:                 
            if(j[move] != 0):           # 크레인이 움직인 곳에 인형이 있다면
                basket.append(j[move])  # 집은 인형을 basket 배열에 삽입
                j[move] = 0             # 인형을 집은 곳을 0으로 초기화
                break                   # 다음 크레인 위치로 이동시키기 위해 break
        if(len(basket) >= 2) : answer += remove_basket_item(basket) # basket에 담긴 인형이 2개 이상이면 점수를 받을 수 있을 지 확인

    return answer

# 입출력 예
# board	                                                        moves	            result
# [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]	[1,5,3,5,1,2,1,4]	4

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))
