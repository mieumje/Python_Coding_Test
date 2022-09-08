def solution(n, lost, reserve):
    answer = 0
    
    students = ['' for _ in range(n + 1)]
    
    for i in reserve:
      if i in lost:
        reserve.remove(i)
        lost.remove(i)
    
    for i in range(1, n+1):
      if i in lost:
        if i - 1 in reserve:
          students[i] = 'O'
          lost.remove(i)
          reserve.remove(i - 1)
          continue
        if i + 1 in reserve:
          students[i] = 'O'
          lost.remove(i)
          reserve.remove(i + 1)
          continue
        students[i] = 'X'
      else:
        students[i] = 'O'
      
    answer = students.count('O')
    
    return answer
  
# n     lost    reserve     return
# 5     [2, 4]  [1, 3, 5]   5
# 5     [2, 4]  [3]         4
# 3     [3]     [1]         2

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))