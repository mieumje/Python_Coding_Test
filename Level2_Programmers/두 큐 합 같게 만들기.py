from collections import deque

def solution(queue1, queue2):
  answer = -1
  queue1 = deque(queue1)
  queue2 = deque(queue2)
  hap = sum(queue1) + sum(queue2)
    
  target = hap // 2
  max_count = len(queue1) + len(queue2)
  curr = sum(queue1)
  cnt = 0
  
  while cnt < max_count:

    if curr < target:
      curr += queue2[0]
      queue1.append(queue2.popleft())
      cnt += 1
    elif curr > target:
      curr -= queue1[0]
      queue2.append(queue1.popleft())
      cnt += 1
    elif curr == target:
      return cnt
  
  return answer

# queue1	      queue2	      result
# [3, 2, 7, 2]	[4, 6, 5, 1]	2
# [1, 2, 1, 2]	[1, 10, 1, 2]	7
# [1, 1]	      [1, 5]	      -1

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))