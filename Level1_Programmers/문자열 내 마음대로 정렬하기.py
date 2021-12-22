def solution(strings, n):
    answer = []
    strings = sorted(strings)
    arr = []
    
    for i in strings:
        arr.append(i[n])
    arr = sorted(arr)
    
    for i in arr:
        for j in strings:
            if i == j[n]:
                answer.append(j)
                strings.remove(j)
                break
            
    
    return answer