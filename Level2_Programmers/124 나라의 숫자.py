# 10진법	124 나라	     10진법	 124 나라
# 1	        1	            6	    14
# 2	        2	            7	    21
# 3	        4	            8	    22
# 4	        11	            9	    24
# 5	        12	            10	    41
#                           11      42
#                           13      111
# 3으로 나누었을 때
# 1인 경우 > +1
# 2인 경우 > +2
# 0인 경우 > +3+1, +1한 만큼 n을 -1
def solution(n):
    answer = ''
    result = []
    while (n > 0):
        mod = n % 3
        if mod == 0:
            mod = 4     # 0인 경우 > +3+1,
            n = n - 1   # +1한 만큼 n을 -1
        result.append(str(mod))
        n = n // 3
    answer = ''.join(result[::-1])
    return answer

# 제한사항
# n은 500,000,000이하의 자연수 입니다.

# 입출력 예
# n	    result
# 1	    1
# 2	    2
# 3	    4
# 4	    11
for i in range(1, 21):
    print(solution(i))
