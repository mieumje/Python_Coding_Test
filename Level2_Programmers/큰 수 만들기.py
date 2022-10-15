from collections import deque

def solution(number, k):
  answer = ''
  arr = deque(number)
  result = [arr.popleft()]
  cnt = 0
  
  while cnt < k:
    value = arr.popleft()
    while result and result[-1] < value and cnt < k:
      result.pop()
      cnt += 1
    result.append(value)

  while arr:
    result.append(arr.popleft())
  
  answer = ''.join(result)
  
  return answer

# number	      k	return
# "1924"	      2	"94"
# "1231234"	    3	"3234"
# "4177252841"	4	"775841"

number = '1231234'
k = 3
print(solution(number, k))