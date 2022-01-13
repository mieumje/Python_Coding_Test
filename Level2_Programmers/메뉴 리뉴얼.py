from itertools import combinations
def make_combinations(orders, course):
    tmp_list = {}
    for i in orders:
        tmp = list(combinations(i,course))
        print(tmp)
        for j in tmp:
            try:
                tmp_list[j] += 1
            except:
                tmp_list[j] = 1
    return [k for k, v in tmp_list.items() if max(tmp_list.values()) == v and max(tmp_list.values()) != 1]

def solution(orders, course):
    answer = []
    for i in course:
        combination_menus = make_combinations(orders, i)
        for j in combination_menus:
            answer.append(''.join(j))
    answer.sort()
    return answer

# [입출력 예]
# orders	                                        course	result
# ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]	[2,3,4]	["AC", "ACDE", "BCFG", "CDE"]
# ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]	[2,3,5]	["ACD", "AD", "ADE", "CD", "XYZ"]
# ["XYZ", "XWY", "WXA"]	                            [2,3,4]	["WX", "XY"]

orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders, course))
