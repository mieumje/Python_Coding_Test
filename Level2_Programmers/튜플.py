def solution(s):
    list = {}
    tmp = ""
    for i in s:
        if i.isdigit():
            tmp += i
        elif tmp:
            try:
                list[int(tmp)] += 1
            except:
                list[int(tmp)] = 1
            tmp = ""

    answer = [k for k in list.keys()]
    
    return answer

# [입출력 예]
# s	                                result
# "{{2},{2,1},{2,1,3},{2,1,3,4}}"	[2, 1, 3, 4]
# "{{1,2,3},{2,1},{1,2,4,3},{2}}"	[2, 1, 3, 4]
# "{{20,111},{111}}"	            [111, 20]
# "{{123}}"	                        [123]
# "{{4,2,3},{3},{2,3,4,1},{2,3}}"	[3, 2, 4, 1]

s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))