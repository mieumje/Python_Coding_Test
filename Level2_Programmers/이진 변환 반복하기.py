def solution(s):
  cnt = 0
  zero_cnt = 0

  while True:
    if s == '1': break
    
    cnt += 1
    zero_cnt += s.count('0')
    s = s.replace('0', '')
    length = len(s)
    s = bin(length)[2:]
    
  answer = [cnt, zero_cnt]
  
  return answer


# s	              result
# "110010101001"	[3,8]
# "01110"	        [3,3]
# "1111111"	      [4,1]

s = '1111111'

print(solution(s))
