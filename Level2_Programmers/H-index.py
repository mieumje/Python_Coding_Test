def solution(citations):
  answer = 0
  if len(citations) == citations.count(0):
    return 0
  
  citations.sort(reverse = True)
  
  for i in range(len(citations)):
    if i + 1 <= citations[i]:
      continue
    else:
      answer = i
      break
  
  if answer == 0:
    answer = len(citations)
  
  return answer

# citations	                return
# [3, 0, 6, 1, 5]	          3
# [6, 5, 5, 5, 3, 2, 1, 0]  4

print(solution(citations=[6, 5, 5, 5, 3, 2, 1, 0]))
print(solution(citations=[4,4,4]))
print(solution(citations=[0,0,0,0,0]))