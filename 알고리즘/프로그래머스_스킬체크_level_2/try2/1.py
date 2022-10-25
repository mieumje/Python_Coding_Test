def solution(s):
  answer = ''
  s = s.lower()
  if not s[0].isdigit():
    s = s.replace(s[0], s[0].upper(), 1)
        
  for i in range(len(s)):
    if s[i - 1] == ' ':
      answer += s[i].upper()
    else: answer += s[i]
  return answer

# s	                      return
# "3people unFollowed me"	"3people Unfollowed Me"
# "for the last week"	    "For The Last Week"

s = "3people unFollowed me"
print(solution(s))