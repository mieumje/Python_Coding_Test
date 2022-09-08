def solution(arr):
    tmp = arr[0]
    answer = [tmp]
    
    for i in range(1, len(arr)):
      if arr[i] == tmp:
        continue
      else:
        tmp = arr[i]
        answer.append(tmp)
    
    return answer
  
# arr             answer
# [1,1,3,3,0,1,1] [1,3,0,1]
# [4,4,4,3,3]     [4,3]

arr = [4,4,4,3,3]

print(solution(arr))