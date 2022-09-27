def solution(n, t, m, p):
  answer = ''
  
  def convert(n, q):
    tmp = '0123456789ABCDEF'

    n, mod = divmod(n, q)
    
    if n == 0:
      return tmp[mod]
    else:
      return convert(n, q) + tmp[mod]
  
  nums = ''
  num = 0
  
  while True:
    if len(nums) > m * t:
      break

    tmp = convert(num, n)
    num += 1
    nums += tmp
  
  while len(answer) < t:
    answer += nums[p - 1]
    p += m
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
p = 2
print(solution(n, t, m, p))
