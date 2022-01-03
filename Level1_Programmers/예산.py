# 부서별로 신청한 금액이 들어있는 배열 d와 예산 budget이 매개변수로 주어질 때, 
# 최대 몇 개의 부서에 물품을 지원할 수 있는지 return 하도록 solution 함수를 완성해주세요.
# 물품을 구매해 줄 때는 각 부서가 신청한 금액만큼 모두 지원해주어야 한다.
# 1,000원인 경우 1,000원 모두 지원, 950원 = X

def solution(d, budget):
    sum, cnt = 0, 0
    
    tmp = sorted(d) # 적음 금액부터 지원하면 최대 부서 수를 구할 수 있음
    
    for i in tmp:
        sum += i
        if sum <= budget:
            cnt += 1
        else:
            break
    
    answer = cnt
    
    return answer

d = [2,2,3,3]
budget = 10
print(solution(d, budget))
# 입출력 예
# d	            budget	    result
# [1,3,2,5,4]	9	        3
# [2,2,3,3]	    10	        4