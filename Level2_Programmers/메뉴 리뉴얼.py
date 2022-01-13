"""
각 손님들이 주문한 단품메뉴들이 문자열 형식으로 담긴 배열 orders, 
"스카피"가 추가하고 싶어하는 코스요리를 구성하는 단품메뉴들의 갯수가 담긴 배열 course가 매개변수로 주어질 때, 
"스카피"가 새로 추가하게 될 코스요리의 메뉴 구성을 문자열 형태로 배열에 담아 return

단, 코스요리 메뉴는 최소 2가지 이상의 단품메뉴로 구성하려고 합니다. 
또한, 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스요리 메뉴 후보에 포함하기로 했습니다.
"""
from itertools import combinations
def make_combinations(orders, course):
    tmp_list = {}
    for i in orders:
        order = ''.join(sorted(i))              # 손님이 주문한 단품메뉴 조합의 문자열을 오름차순 정렬
        tmp = list(combinations(order,course))  # 단품메뉴 조합에서 course개 만큼 조합
        for j in tmp:
            try:
                tmp_list[j] += 1                # 해당 조합 메뉴가 있다면 +1
            except:
                tmp_list[j] = 1                 # 해당 조합 메뉴가 없다면 1로 초기화
           # 각 조합이 담긴 tmp_list에서 value(조합의 개수)가 큰 것을 return
           # 이 때, 조합의 value(개수)가 1인 경우는 최소 2명 이상의 손님에게서 주문된 구성만 코스요리 후보에 들어가므로 제외
    return [k for k, v in tmp_list.items() if max(tmp_list.values()) == v and max(tmp_list.values()) != 1]

def solution(orders, course):
    answer = []
    for i in course:
        combination_menus = make_combinations(orders, i) # 코스요리를 구성하는 단품메뉴들의 갯수 만큼 조합을 생성
        for j in combination_menus:                      # 완성된 조합 메뉴를 반복하면서
            answer.append(''.join(j))                    # answer 배열에 push
    answer.sort()
    return answer

# [제한사항]
# orders 배열의 크기는 2 이상 20 이하입니다.
# orders 배열의 각 원소는 크기가 2 이상 10 이하인 문자열입니다.
# 각 문자열은 알파벳 대문자로만 이루어져 있습니다.
# 각 문자열에는 같은 알파벳이 중복해서 들어있지 않습니다.
# course 배열의 크기는 1 이상 10 이하입니다.
# course 배열의 각 원소는 2 이상 10 이하인 자연수가 오름차순으로 정렬되어 있습니다.
# course 배열에는 같은 값이 중복해서 들어있지 않습니다.
# 정답은 각 코스요리 메뉴의 구성을 문자열 형식으로 배열에 담아 사전 순으로 오름차순 정렬해서 return 해주세요.
# 배열의 각 원소에 저장된 문자열 또한 알파벳 오름차순으로 정렬되어야 합니다.
# 만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아 return 하면 됩니다.
# orders와 course 매개변수는 return 하는 배열의 길이가 1 이상이 되도록 주어집니다.

# [입출력 예]
# orders	                                        course	result
# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]	                            [2,3,4]	["WX", "XY"]

# 입출력 예에 대한 설명
# 손님 번호	    주문한 단품메뉴 조합
# 1번 손님	    A, B, C, F, G
# 2번 손님	    A, C
# 3번 손님	    C, D, E
# 4번 손님	    A, C, D, E
# 5번 손님	    B, C, F, G
# 6번 손님	    A, C, D, E, H
# 가장 많이 함께 주문된 단품메뉴 조합에 따라 "스카피"가 만들게 될 코스요리 메뉴 구성 후보는 다음과 같습니다.

# 코스 종류	        메뉴 구성	    설명
# 요리 2개 코스	    A, C	        1번, 2번, 4번, 6번 손님으로부터 총 4번 주문됐습니다.
# 요리 3개 코스	    C, D, E	        3번, 4번, 6번 손님으로부터 총 3번 주문됐습니다.
# 요리 4개 코스	    B, C, F, G	    1번, 5번 손님으로부터 총 2번 주문됐습니다.
# 요리 4개 코스	    A, C, D, E	    4번, 6번 손님으로부터 총 2번 주문됐습니다.
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))