def solution(msg):
  answer = []
  
  dict = {}
  idx = 0
  
  for i in range(65, 91):
    idx += 1
    dict[chr(i)] = idx
  
  while msg:
    i = 1
    while True:
      if i > len(msg): break
      if not msg[:i] in dict.keys():
        break
      i += 1
    answer.append(dict[msg[:i-1]])
    dict[msg[:i]] = len(dict) + 1
    
    msg = msg[i-1:]
        
  return answer

# msg	                        answer
# KAKAO	                      [11, 1, 27, 15]
# TOBEORNOTTOBEORTOBEORNOT	  [20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
# ABABABABABABABAB	          [1, 2, 27, 29, 28, 31, 30]

msg = 'TOBEORNOTTOBEORTOBEORNOT'

print(solution(msg))