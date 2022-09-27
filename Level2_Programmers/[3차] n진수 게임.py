def solution(n, t, m, p):
  answer = ''
  
  def convert(n, q):
    rev_base = ''
    
    while n > 0:
      n, mod = divmod(n, q)
      rev_base += str(mod)
    
    return rev_base[::-1]
  
  nums = '0'
  num = 1
  
  while True:
    if len(nums) > m * t:
      break
    if n == 16:
      tmp = hex(num)[2:]
    elif n == 10:
      tmp = str(num)
    elif n == 8:
      tmp = oct(num)[2:]
    elif n == 2:
      tmp = bin(num)[2:]
    else:
      tmp = convert(num, n)
    num += 1
    nums += tmp
  # print(nums)
  turn = 0
  for i in nums:
    turn += 1
  
    if len(answer) == t:
      break
    if turn == p:
      answer += i if not i.isalpha() else i.upper()
      
    if turn >= m:
      turn = 0
      
  return answer

# n	  t	  m	  p	  result
# 2	  4	  2	  1	  "0111"
# 16	16	2	  1	  "02468ACE11111111"
# 16	16	2	  2	  "13579BDF01234567"

n = 2
t = 4
m = 2
p = 1
print(solution(n, t, m, p))

n = 16
t = 16
m = 2
p = 1
print(solution(n, t, m, p))
