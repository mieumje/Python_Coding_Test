def solution(n):
  answer = 0
  one_count = bin(n)[2:].count('1')
  n += 1
  while True:
    if n > 1000000: break
    
    if bin(n)[2:].count('1') == one_count:
      answer = n
      break
    else:
      n += 1
  return answer

# n	  result
# 78	83
# 15	23

n = 15

print(solution(n))