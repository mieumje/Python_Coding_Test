def solution(queue1, queue2):
  answer = -1
  hap = sum(queue1) + sum(queue2)
  target = hap // 2
  max_count = len(queue1) + len(queue2)
  cnt = 0
  
  while cnt < max_count:

    if sum(queue1) < target:
      queue1.append(queue2.pop(0))
      cnt += 1
    elif sum(queue1) > target:
      queue2.append(queue1.pop(0))
      cnt += 1
    elif sum(queue1) == target:
      return cnt
  
  return answer

# queue1	      queue2	      result
# [3, 2, 7, 2]	[4, 6, 5, 1]	2
# [1, 2, 1, 2]	[1, 10, 1, 2]	7
# [1, 1]	      [1, 5]	      -1

queue1 = [1, 1]
queue2 = [1, 5]

print(solution(queue1, queue2))