def solution(x):
    tmp = str(x)
    hap = 0
    for i in tmp:
        hap += int(i)
    
    answer = True if x % hap == 0 else False
    
    return answer