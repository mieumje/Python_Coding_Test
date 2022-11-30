def solution(topping):
  answer = 0
  for i in range(1, len(topping)):
    left, right = topping[:i], topping[i:]
    left_length, right_length = len(list(set(left))), len(list(set(right)))
    
    if left_length == right_length:
      answer += 1
  return answer

# topping	                  result
# [1, 2, 1, 3, 1, 4, 1, 2]	2
# [1, 2, 3, 1, 4]	          0

topping = [1, 2, 1, 3, 1, 4, 1, 2]

print(solution(topping))