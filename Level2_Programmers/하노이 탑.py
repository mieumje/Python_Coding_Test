def solution(n):
  def hanoi(n, start, via, end, answer = []):
    if n == 1:
      answer.append([start, end])
      return answer
    
    answer = hanoi(n - 1, start, end, via, answer)
    answer.append([start, end])
    answer = hanoi(n - 1, via, start, end, answer)
    
    return answer

  answer = hanoi(n, 1, 2, 3, answer = [])

  return answer

# n	result
# 2	[ [1,2], [1,3], [2,3] ]

n = 3
print(solution(n))