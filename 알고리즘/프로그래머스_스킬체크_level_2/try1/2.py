import math


def solution(progresses, speeds):
  answer = []
  times = []
  
  for i in range(len(progresses)):
    d = math.ceil((100 - progresses[i]) / speeds[i])
    times.append(d)
  
  cnt = 1
  curr = times[0]
  
  for i in range(1, len(times)):
    if curr < times[i]:
      curr = times[i]
      answer.append(cnt)
      cnt = 1
    else:
      cnt += 1
  
  if cnt > 0:
    answer.append(cnt)
  
  return answer

# progresses	              speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))