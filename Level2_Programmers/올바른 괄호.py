def solution(s):
  answer = False
  
  stack = []
  
  if s[0] == ')': 
    return answer
  
  for i in s:
    if i == '(':
      stack.append(i)
      
    if i == ')' and len(stack):
      stack.pop()
  
  answer = True if len(stack) == 0 else False
  
  return answer

# s	        answer
# "()()"	  true
# "(())()"	true
# ")()("	  false
# "(()("	  false

s = ")"	

print(solution(s))