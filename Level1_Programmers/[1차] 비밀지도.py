def ten_to_two(x, n):
    tmp = ''
    while x > 0 :
        x, mod = divmod(x,2)    # 몫, 나머지
        tmp += str(mod)
    
    if len(tmp) < n :
        while len(tmp) < n :
            tmp += '0'          # n 만큼 빈 자리수는 0으로 채움
    return tmp[::-1]            # 역순


def solution(n, arr1, arr2):
    answer = []
    
    for i in range(0, n):
        x, y = ten_to_two(arr1[i], n), ten_to_two(arr2[i], n)
        result = ""
        for j in range(0, n):
            if x[j] == '1' or y[j] == '1':
                result += "#"
            elif x[j] == '0' or y[j] == '0':
                result += " "
        answer.append(result)
            
    return answer

# 매개변수	    값
# n	            5
# arr1	        [9, 20, 28, 18, 11]
# arr2	        [30, 1, 21, 17, 28]
# 출력	        ["#####","# # #", "### #", "# ##", "#####"]

# 매개변수	    값
# n	            6
# arr1	        [46, 33, 33 ,22, 31, 50]
# arr2	        [27 ,56, 19, 14, 14, 10]
# 출력	        ["######", "### #", "## ##", " #### ", " #####", "### # "]

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n, arr1, arr2))