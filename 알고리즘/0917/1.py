def solution(bricks):
  answer = []
    
  for i in range(0, len(bricks)):
    brick = sum(bricks[:i+1])
    hap = 0
    cnt = 1
    
    for j in bricks[i + 1:]:
      hap += j
      if hap > brick:
        break;
      
      if hap == brick:
        hap = 0
        cnt += 1
    if hap == 0:
      print(brick, cnt)
      answer.append(cnt)

  answer.sort()

  return answer

# bricks
# [1,1,1,1,1,1]
# [2,1,1,2]
# [1,2,3,2,1]

bricks = [2,1,1,2]

print(solution(bricks))