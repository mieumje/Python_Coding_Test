def solution(topping):
  from collections import Counter
  answer = 0
  left = set()
  right = Counter(topping)
  
  while topping:
    item = topping.pop(0)
    left.add(item)

    if right[item] > 1:
      right[item] -= 1
    else:
      del right[item]
    
    if len(left) > len(right):
      break

    answer += 1 if len(left) == len(right) else 0
  
  return answer

# topping	                  result
# [1, 2, 1, 3, 1, 4, 1, 2]	2
# [1, 2, 3, 1, 4]	          0

topping = [1, 2, 1, 3, 1, 4, 1, 2]

print(solution(topping))