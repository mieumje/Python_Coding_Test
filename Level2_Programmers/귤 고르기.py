def solution(k, tangerine):
  answer = 0
  
  if k == 1:
    return 1
  
  arr = [[i + 1, 0] for i in range(max(tangerine))]
  
  for t in tangerine:
    arr[t - 1][1] += 1
  
  arr = sorted(arr, key = lambda x : -x[1])
  idx = 0
  while True:
    if k <= 0: break
    k -= arr[idx][1]
    answer += 1
    
  return answer

# k	tangerine	                result
# 6	[1, 3, 2, 5, 4, 5, 2, 3]	3
# 4	[1, 3, 2, 5, 4, 5, 2, 3]	2
# 2	[1, 1, 1, 1, 2, 2, 2, 3]	1

k = 2
tangerine = [1, 1, 1, 1, 2, 2, 2, 3]

print(solution(k, tangerine))