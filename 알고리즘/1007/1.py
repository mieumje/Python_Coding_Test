def solution(samDaily, kellyDaily, difference):
  if samDaily >= kellyDaily:
    return -1
  s, k = 0, 0
  initial_samDaily = samDaily

  cnt = 0

  while True:
    if s < k:
      break
    cnt += 1
    k += kellyDaily
    if cnt == 1:
      s += (difference + initial_samDaily)
    else:
      s += initial_samDaily

  return cnt


# samDaily  kellyDaily difference return
# 4         5           1           2
# 3         6           6           3
# 3         5           1           1
# 100       100         0           -1

samDaily = 100
kellyDaily = 100
difference = 0

print(solution(samDaily,kellyDaily,difference))