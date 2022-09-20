def solution(people, limit):
  answer = 0
  people.sort()

  left = 0
  right = len(people) - 1
  
  while(left < right):
    sum = people[left] + people[right]
    
    if sum > limit:
      right -= 1
    else:
      right -= 1
      left += 1
    
    answer += 1
  
  answer = answer if left != right else answer + 1
  
  return answer


# people	          limit	return
# [70, 50, 80, 50]	100	  3
# [70, 80, 50]	    100	  3

people = [40, 40, 40, 50, 70, 80, 100]
limit = 100

print(solution(people, limit))