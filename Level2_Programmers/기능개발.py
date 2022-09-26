import math
def solution(progresses, speeds):
  answer = []
  speed = math.ceil((100 - progresses[0]) / speeds[0])
  complete = 1
  
  for i in range(1, len(progresses)):
    curr = math.ceil((100 - progresses[i]) / speeds[i])
    if speed >= curr:
      complete += 1
      
    else:
      speed = curr
      answer.append(complete)
      complete = 1
    
  answer.append(complete)
  
  return answer


# 입출력 예
# progresses	            speeds	            return
# [93, 30, 55]	            [1, 30, 5]	        [2, 1]
# [95, 90, 99, 99, 80, 99]	[1, 1, 1, 1, 1, 1]	[1, 3, 2]

progresses = [95, 90, 99, 99, 80, 99]	
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progresses, speeds))