from itertools import permutations
def plus_minus_multiply(num1,num2,operation): # 리스트에 담긴 숫자는 문자열 형태
    if operation == "+":
        return int(num1) + int(num2)
    elif operation == "*":
        return int(num1) * int(num2)
    elif operation == "-":
        return int(num1) - int(num2)

def cal(expression,op):
    tmp_num = ""
    exp = []
    for i in expression:    # 입력 받은 문자열을 숫자와 연산자로 분리
        if i.isdigit():
            tmp_num += i
        else:
            exp.append(tmp_num)
            exp.append(i)
            tmp_num = ""
    exp.append(tmp_num)     # 마지막 숫자 push
    
    for o in op:            # 연산 우선순위에 따라 반복문 실행, ["*,-,+", "*,+,-", "-,*,+", "-,+,*", "+,*,-", "+,-,*"]
        s = []              # stack을 위한 빈 리스트 // 우선순위 연산을 한 나머지 숫자와 연산자들
        while exp:          # 숫자, 연산자로 분리된 expression이 empty가 될 때까지 반복
            tmp = exp.pop(0)
            if tmp == o:    # 연산자가 나오면 계산
                s.append(plus_minus_multiply(s.pop(), exp.pop(0), o))   # stack에 담긴 숫자, 연산자 다음 숫자, 연산자 // 연산자 기준 왼쪽 숫자, 연산자 기준 다음 숫자, 연산자
            else:           # 연산자가 아니면 숫자를 stack에 push
                s.append(tmp)
        exp = s             # 우선순위 연산자 수행 후, 다음 연산자 수행을 위해 exp 리스트 stack으로 초기화
    return abs(exp[0])      # 모든 연산 후, 계산 된 값의 절대값 return

def solution(expression):
    res = []
    operations = ["*","-","+"]
    for i in permutations(operations):  # *, -, +로 조합 할 수 있는 연산의 순서
        res.append(cal(expression,i))   # 우선순위가 지정된 연산자 리스트 순서에 따라 수식 계산
    
    return max(res)                     # res 리스트에 담긴 최댓값 return

# 입출력 예
# expression	        result
# "100-200*300-500+20"	60420
# "50*6-3*2"	        300

expression = "100-200*300-500+20"
print(solution(expression))
