# 2016년 1월 1일은 금요일
# 2016년 a월 b일은 무슨 요일?
# answer = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
# ex) a = 5, b = 24 -> 5월 24일은 화요일 -> return "TUE"

# 제한 조건
# 2016년은 윤년입니다.
# 2016년 a월 b일은 실제로 있는 날입니다. (13월 26일이나 2월 45일같은 날짜는 주어지지 않습니다)

def solution(a, b):
    #"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"
    # 1월 1일 = 금요일
    # 1,3,5,7,8,10,12월 = 31일
    # 4,6,9,11 = 30일
    # 2월 = 29일
    answer = {
        1 : "FRI",
        2 : "SAT",
        3 : "SUN",
        4 : "MON",
        5 : "TUE",
        6 : "WED",
        0 : "THU"
    }
    days = 0
    
    for i in range(1,a):
        if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
            days += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            days += 30
        elif i == 2:
            days += 29
    days += b
    day = days % 7
    
    return answer[day]

# 입출력 예
# a	    b	    result
# 5	    24	    "TUE"

print(solution(5,24))