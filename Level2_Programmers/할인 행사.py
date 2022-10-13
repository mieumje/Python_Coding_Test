def solution(want, number, discount):
  answer = 0
  for i in want:
    if i not in discount:
      return 0
    
  for i in range(len(discount) - 9):
    tmp = []
    for j in want:
      tmp.append(discount[i:(i + 10)].count(j))
    answer += 1 if tmp == number else 0
  return answer

# want	                                      number	        discount	                                                                                                                      result
# ["banana", "apple", "rice", "pork", "pot"]	[3, 2, 2, 2, 1]	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]	3
# ["apple"]	                                  [10]	          ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]	                          0

want = ["banana", "apple", "rice", "pork", "pot"]	
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount))