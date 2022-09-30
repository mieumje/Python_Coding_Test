def solution(dirs):
  records = set()
  cur_x, cur_y = 0, 0
  for dir in dirs:
    if dir == 'U' and cur_y < 5:
      records.add(((cur_x, cur_y), (cur_x, cur_y + 1)))
      cur_y += 1    
    elif dir == 'D' and cur_y > -5:
      records.add(((cur_x, cur_y - 1), (cur_x, cur_y)))
      cur_y -= 1  
    elif dir == 'R' and cur_x < 5:
      records.add(((cur_x, cur_y), (cur_x + 1, cur_y)))
      cur_x += 1 
    elif dir == 'L' and cur_x > -5:
      records.add(((cur_x - 1, cur_y), (cur_x, cur_y)))
      cur_x -= 1
      
  answer = len(records)
  return answer

# dirs	      answer
# "ULURRDLLU"	7
# "LULLLLLLU"	7

dirs = "LULLLLLLU"

print(solution(dirs))
