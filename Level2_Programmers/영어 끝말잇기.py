def solution(n, words):
  answer = []
  dict = {}
  idx = 0
  count = [0 for _ in range(n + 1)]
  
  for i in range(len(words)):
    idx += 1
    if idx > n: idx = 1
    
    if i > 0:
      prev, curr = words[i - 1], words[i]
      if prev[-1] != curr[0]:
        answer = [idx, count[idx] + 1]
        break
    
    if not words[i] in dict:
      dict[words[i]] = True
      count[idx] = count[idx] + 1
      continue
    
    if words[i] in dict:
      answer = [idx, count[idx] + 1]
      break
  
  answer = [0, 0] if len(answer) == 0 else answer
  
  return answer

# n	words	                                                                        result
# 3	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]	[3,3]
# 5	["hello", "observe", "effect", "take", "either", "recognize", 
#    "encourage", "ensure", "establish", "hang", "gather", "refer", 
#    "reference", "estimate", "executive"]	                                      [0,0]
# 2	["hello", "one", "even", "never", "now", "world", "draw"]	                    [1,3]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n, words))