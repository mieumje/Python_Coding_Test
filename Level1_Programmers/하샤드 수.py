# x의 자릿수의 합으로 x가 나누어져야 함
# 18 > 1 + 8 = 9, 18 % 9 = 0 하샤드 수
# 1 <= x <= 10,000
# 하샤드 수 true 아니면 false  

def hap(x):
    sum = 0
    for i in x:
        sum += int(i)
    return sum

def solution(x):
    tmp = str(x)
    num = hap(tmp)
    if(x % num == 0):
        return True
    else:
        return False


# arr	return
# 10	true
# 12	true
# 11	false
# 13	false

