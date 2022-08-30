def solution(numbers):
    answer = []
    
    for x in range(len(numbers) - 1):
      tmp = numbers[x]
      for y in range(x + 1, len(numbers)):
        value = tmp + numbers[y]
        if value not in answer:
          answer.append(value)

    answer.sort()
    
    return answer
  
# numbers       result
# [2,1,3,4,1]   [2,3,4,5,6,7]
# [5,0,2,7]     [2,5,7,9,12]

numbers = [2,1,3,4,1]

print(solution(numbers))