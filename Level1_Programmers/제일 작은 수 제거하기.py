def solution(arr):
    tmpMin = min(arr)
    arr.remove(tmpMin)
    if(len(arr) == 0):
        return [-1]
    return arr

arr = [4,3,2,1]
print(solution(arr))

arr = [10]
print(solution(arr))
