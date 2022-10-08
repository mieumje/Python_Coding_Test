from collections import deque

def solution(bridge_length, weight, truck_weights):
  answer = 0
  q = deque(truck_weights)
  arr = [0] * bridge_length
  weight_sum = 0
  
  while arr:
    answer += 1
    if arr[0] != 0:
      weight_sum -= arr[0]
    arr.pop(0)
    
    if len(q):
      if (weight_sum + q[0]) <= weight:
        weight_sum += q[0]
        arr.append(q.popleft())  
        continue
      arr.append(0)
      
  return answer

# bridge_length	weight	truck_weights	                  return
# 2	            10	    [7,4,5,6]	                      8
# 100	          100	    [10]	                          101
# 100	          100	    [10,10,10,10,10,10,10,10,10,10]	110

bridge_length = 100
weight = 100
truck_weights = [10] * 10	  

print(solution(bridge_length, weight, truck_weights))