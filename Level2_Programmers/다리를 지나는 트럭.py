from collections import deque

def solution(bridge_length, weight, truck_weights):
  answer = 0
  q = deque(truck_weights)
  arr = [0] * bridge_length
  
  while arr:
    answer += 1
    arr.pop(0)
    
    if len(q):
      if (sum(arr) + q[0]) <= weight:
        arr.append(q.popleft())  
        continue
      arr.append(0)
      
  return answer

# bridge_length	weight	truck_weights	                  return
# 2	            10	    [7,4,5,6]	                      8
# 100	          100	    [10]	                          101
# 100	          100	    [10,10,10,10,10,10,10,10,10,10]	110

bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]	  

print(solution(bridge_length, weight, truck_weights))