from collections import deque


def solution(s):
  answer = len(s) - 1
  arr = deque(s)
  dd = [')', ']', '}']
  
  for x in range(len(arr) - 1):
    if x != 0 : arr.append(arr.popleft())
    if arr[0] == ')' or arr[0] == ']' or arr[0] == '}':
      answer -= 1
      continue
    stack = []
    
    for y in arr:
      if y == '(' or y == '[' or y == '{':
        stack.append(y)
        continue
      if len(stack) == 0 and y in dd:
        answer -= 1
        break
      
      if y == ')' and stack[-1] == '(':
        stack.pop()
        continue
      
      if y == ']' and stack[-1] == '[':
        stack.pop()
        continue
      
      if y == '}' and stack[-1] == '{':
        stack.pop()
        continue
    
    if len(stack) > 0: 
      answer -= 1
    
  return answer

# s	        result
# "[](){}"	3
# "}]()[{"	2
# "[)(]"	  0
# "}}}"	    0

s = "}]()[{"

print(solution(s))