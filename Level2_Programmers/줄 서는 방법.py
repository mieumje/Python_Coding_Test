from itertools import permutations
def solution(n, k):
  arr = [i for i in range(1, n + 1)]
  lists = list(permutations(arr, len(arr)))
  answer = [i for i in lists[k - 1]]
    
  return answer

# n	k	result
# 3	5	[3,1,2]

n = 3
k = 5
print(solution(n, k))