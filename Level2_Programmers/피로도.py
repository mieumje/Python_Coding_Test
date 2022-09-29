from itertools import permutations

def solution(k, dungeons):
  answer = -1
  new_list = list(permutations(dungeons, len(dungeons)))
  arr = []
  for i in new_list:
    limit = k
    cnt = 0
    for j in i:
      required, consumption = j
      if limit >= required:
        limit -= consumption
        cnt += 1
      else:
        break
    arr.append(cnt)

  answer = max(arr)
  return answer

# k	  dungeons	                result
# 80	[[80,20],[50,40],[30,10]]	3

print(solution(k=80, dungeons=[[80,20],[50,40],[30,10]]))