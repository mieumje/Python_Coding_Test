def solution(citations):
  answer = 0
    
  h_index = 0
  
  while True:
    high_cnt = 0
    low_cnt = 0
    for i in citations:
      if h_index >= i:
        high_cnt += 1
      else:
        low_cnt += 1
    
    if low_cnt <= h_index and h_index <= high_cnt:
      break
    
    h_index += 1
    
  answer = h_index
  
  return answer

# citations	                return
# [3, 0, 6, 1, 5]	          3
# [6, 5, 5, 5, 3, 2, 1, 0]  4

print(solution(citations=[3, 0, 6, 1, 5]))