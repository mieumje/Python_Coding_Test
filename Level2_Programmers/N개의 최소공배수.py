def solution(arr):
  answer = 0
  arr.sort()
  tmp = max(arr)
  cnt = 0
  
  while True:
    cnt += 1
    length = 0
    maximum = tmp * cnt
    for i in arr[:-1]:
      if maximum % i == 0:
        length += 1
        continue
      else:
        break
    if length == len(arr[:-1]):
      break;
  answer = maximum
  return answer


# arr	        result
# [2,6,8,14]	168
# [1,2,3]	    6

arr = [2,6,8,14]

print(solution(arr))