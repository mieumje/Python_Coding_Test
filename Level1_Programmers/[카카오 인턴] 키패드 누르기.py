"""
맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
    4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.
순서대로 누를 번호가 담긴 배열 numbers, 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return
"""
# 1  2  3
# 4  5  6
# 7  8  9
# 10 11 12

def solution(numbers, hand):
    answer = ""
    left = 10       # 왼손 위치
    right = 12      # 오른손 위치
    for i in numbers:
        number = i                      # 눌러야 할 다음 번호
        if number == 0 : number = 11    # 눌러야 할 번호가 0 이면 11로 바꿈
        if number == 1 or number == 4 or number == 7:   # 1, 4, 7 -> 왼손
            answer += "L"
            left = number
        elif number == 3 or number == 6 or number == 9: # 3, 6, 9 -> 오른손
            answer += "R"
            right = number
        else:                           # 2, 5, 8, 0(11)
            absL = abs(number - left)   # 현재 왼손 위치에서 눌러야 할 다음 번호까지의 차의 절대값
            absR = abs(number - right)  # 현재 오른손 위치에서 눌러야 할 다음 번호까지의 차의 절대값
            distance_to_number_L = (absL // 3) + (absL % 3) # 왼손에서 눌러야 할 다음 번호까지의 거리
            distance_to_number_R = (absR // 3) + (absR % 3) # 오른손에서 눌러야 할 다음 번호까지의 거리
                                                            # // 3 : 상하 움직임, % 3 : 좌우 움직임
            if distance_to_number_L > distance_to_number_R:
                answer += "R"
                right = number
            elif distance_to_number_R > distance_to_number_L:
                answer += "L"
                left = number
            else:
                if hand == "right":
                    answer += "R"
                    right = number
                else:
                    answer += "L"
                    left = number
    return answer

# hand는 "left" 또는 "right" 입니다.
# "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.

# 입출력 예
# numbers	                        hand	result
# [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]	"right"	"LRLLLRLLRRL"
# [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]	"left"	"LRLLRRLLLRR"
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]	"right"	"LLRLLRLLRL"
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers,hand))

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
print(solution(numbers,hand))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = "right"
print(solution(numbers,hand))