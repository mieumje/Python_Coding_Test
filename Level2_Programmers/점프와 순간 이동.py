def solution(n):
  ans = 0
  
  while True:
    if n <= 2: break
    if n % 2 == 0:
      n /= 2
    else:
      n -= 1
      ans += 1
      
  return ans + 1

# N	    result
# 5	    2
# 6	    2
# 5000	5


print(solution(6))
print(solution(5))
print(solution(5000))