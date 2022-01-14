def solution(numbers):
    numbers = list(map(str,numbers))
    nums = sorted(numbers, key=lambda x:x*3 ,reverse=True)
    answer = str(int(''.join(nums)))
    return answer

# 입출력 예
# numbers	        return
# [6, 10, 2]	    "6210"
# [3, 30, 34, 5, 9]	"9534330"
numbers = [1, 10, 100]
print(solution(numbers))