def solution(N):
  if N <= 99:
    return N
  
  answer = N

  for i in range(100, N+1):
    tmp = list(str(i))
    D = int(tmp[0]) - int(tmp[1])
    for j in range(2, len(tmp)):
      if int(tmp[j - 1]) - int(tmp[j]) != D:
        answer -= 1
        break
  
  return answer

N = int(input())

print(solution(N))