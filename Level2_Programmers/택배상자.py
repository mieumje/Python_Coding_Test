def solution(order):
  answer = 0
  index = 0
  tmp = []
  truck = []

  for i in range(1, len(order) + 1):
    if order[index] != i:
      tmp.append(i)
      continue
    truck.append(order[index])
    index += 1

    while True:
      if not len(tmp) or tmp[-1] != order[index]:
        break
      truck.append(tmp.pop())
      index += 1

  answer = len(truck)
  return answer
# order   	      result
# [4, 3, 1, 2, 5]	2
# [5, 4, 3, 2, 1]	5


order = [4, 3, 1, 2, 5]

print(solution(order))
