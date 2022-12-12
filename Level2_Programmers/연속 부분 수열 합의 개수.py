def solution(elements):
  answer = 0
  length = len(elements)

  arr = elements + elements
  result = set()

  for i in range(length):
    for j in range(length):
      hap = sum(arr[j : j + i + 1])
      result.add(hap)
  
  answer = len(result)

  return answer

# elements	  result
# [7,9,1,1,4]	18

elements = [7,9,1,1,4]
print(solution(elements))