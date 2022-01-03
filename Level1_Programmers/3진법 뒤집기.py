def ten_to_three(n,q):
    answer = ""
    
    while n>0:
        n, mod = divmod(n,q)
        answer += str(mod)
    
    # 10진법 수를 n진법 수로 바꾸고 return 할 경우 역순으로 출력해야 하지만, 
    # 문제에서 3진법으로 바꾸고 역순의 수를 10진법으로 바꾸기 때문에 역순 그대로 return
    return answer 


def solution(n):
    tmp = ten_to_three(n,3)
    
    answer = int(tmp,3)
    
    return answer

n = 45
print(solution(n))

# 입출력 예
# n	    result
# 45	7
# 125	229


"""

입출력 예 설명

입출력 예 #1

답을 도출하는 과정은 다음과 같습니다.
n (10진법)	n (3진법)	앞뒤 반전(3진법)	10진법으로 표현
45	1200	0021	7
따라서 7을 return 해야 합니다.

"""