def solution(arrayA, arrayB):
  def gcd(a, b):
    while b != 0:
      a, b = b, a%b
    return a
  
  left_max = 0
  right_max = 0  
  left_GCD = arrayA[0]
  right_GCD = arrayB[0]
  length = len(arrayA)
  
  for i in range(length):
    left_GCD = gcd(left_GCD, arrayA[i])
    right_GCD = gcd(right_GCD, arrayB[i])
  
  for i in range(length):
    if arrayB[i] % left_GCD == 0:
      left_max = 0
      break
    left_max = left_GCD
    
  for i in range(length):
    if arrayA[i] % right_GCD == 0:
      right_max = 0
      break
    right_max = right_GCD
  
  answer = 0 if left_max == 0 and right_max == 0 else max(left_max, right_max)
  return answer

# arrayA	      arrayB	      result
# [10, 17]	    [5, 20]     	0
# [10, 20]	    [5, 17]     	10
# [14, 35, 119]	[18, 30, 102]	7

arrayA = [14, 35, 119]
arrayB = [18, 30, 102]

print(solution(arrayA, arrayB))