def solution(brown, yellow):
  answer = []
  height = 0
  
  if yellow % 2 != 0 and (yellow * 2) + 6 == brown:
    answer = [yellow + 2, 3]
    return answer
  
  while True:
    height += 1
    if yellow % height == 0: 
      width = yellow // height
    else:
      continue
    
    if height > width: break
    
    perimeter = (width * 2) + (height * 2) + 4
    print(width, height, perimeter)
    
    if perimeter == brown:
      answer = [width + 2, height + 2]
      break
    
      
  return answer

# brown	  yellow	return
# 10	    2	      [4, 3]
# 8	      1	      [3, 3]
# 24	    24	    [8, 6]

brown = 8
yellow = 1
print(solution(brown, yellow))
