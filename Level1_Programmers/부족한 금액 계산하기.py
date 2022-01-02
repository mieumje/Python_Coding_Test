# 놀이기구 처음 이용료는 price
# N번째 이용시 원래 이용료의 N배
# ex) 100원, 3번 -> 100원, 200원, 300원
# N번 이용시 모자라는 금액 return, 모자라지 않은 경우 0 return

def solution(price, money, count):
    answer = 0
    
    sum = 0
    for i in range(1, count+1):
        sum += price * i
    
    if sum > money:
        answer = sum - money
    else:
        return answer
    
    return answer

# 제한사항
# 놀이기구의 이용료 price : 1 ≤ price ≤ 2,500, price는 자연수
# 처음 가지고 있던 금액 money : 1 ≤ money ≤ 1,000,000,000, money는 자연수
# 놀이기구의 이용 횟수 count : 1 ≤ count ≤ 2,500, count는 자연수

# 입출력 예
# price	money	count	result
# 3	    20	    4	    10