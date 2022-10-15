from collections import deque

def solution(number, k):
  answer = ''
  arr = deque(number)
  result = [arr.popleft()]
   
  while arr:
    value = arr.popleft()
    while result and result[-1] < value and k != 0:
      result.pop()
      k -= 1
    result.append(value)
  
  while k and result:
    result.pop()
    k -= 1
  
  answer = ''.join(result)
  
  return answer

# number	      k	return
# "1924"	      2	"94"
# "1231234"	    3	"3234"
# "4177252841"	4	"775841"
# "654321"      1 "65432"
# "654321"      5 "6"

number = '4177252841'
k = 4
print(solution(number, k))