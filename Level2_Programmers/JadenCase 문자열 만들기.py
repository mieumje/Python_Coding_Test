def solution(s):
  answer = ' '
  
  arr = s.split(' ')  
  idx = 0
  
  for word in arr:
    if word[0].isdigit():
      word = word[0] + word[1:].lower()
    else:
      word = word[0].upper() + word[1:].lower()
    
    arr[idx] = word
    idx += 1
  
  answer = answer.join(arr)
  
  return answer


# s	                        return
# "3people unFollowed me"	  "3people Unfollowed Me"
# "for the last week"	      "For The Last Week"

s = "3people unFollowed me"

print(solution(s))