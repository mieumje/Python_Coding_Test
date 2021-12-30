# 자연수 x 부터 시작해 x씩 증가하는 숫자를 n개 지나는 리스트를 return


# x	n	answer
# 2	5	[2,4,6,8,10]
# 4	3	[4,8,12]
#-4	2	[-4, -8]
def solution(x, n):
    answer = []
    tmp = x
    for i in range(0, n):
        answer.append(tmp)
        tmp += x
    return answer

print(solution(2,5))