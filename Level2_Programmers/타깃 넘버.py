"""
n개의 음이 아닌 정수가 있습니다. 
이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.
"""

def solution(numbers, target):
    answer = 0
    arr = [0]   # 첫 번째 인덱스 요소를 더하고, 빼기 위한 0
    for i in numbers:
        tmp = []    
        for j in arr:   # 더하기, 빼기 연산을 한 결과가 담긴 배열을 탐색
            tmp.append(j + i)   # 해당 인덱스 값에 더하기
            tmp.append(j - i)   # 해당 인덱스 값에 빼기
        arr = tmp               # 연산 후 arr 갱신
    
    answer = arr.count(target)
    return answer

# 입출력 예
# numbers	        target	return
# [1, 1, 1, 1, 1]	3	    5
numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers,target))