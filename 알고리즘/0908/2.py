def solution(n, lost, reserve):
    answer = 9999
    
    students = [1 for _ in range(n + 1)]
    students[0] = None
    print(students[1:])
    for i in lost:
      students[i] = students[i] - 1
    print(students[1:])
    for i in reserve:
      students[i] = students[i] + 1
  
    print(students[1:])
    for i in range(1, len(students)):
      if students[i] == 0 and i - 1 > 0 and students[i - 1] == 2:
        students[i - 1] = students[i -1] - 1
        students[i] = students[i] + 1
        continue
      if students[i] == 0 and i + 1 < n + 1 and students[i + 1] == 2:
        students[i + 1] = students[i + 1] - 1
        students[i] = students[i] + 1
        continue
      
    print(students[1:])
    answer = n - students[1:].count(0)
    
      
    return answer
    
  
# n     lost    reserve     return
# 5     [2, 4]  [1, 3, 5]   5
# 5     [2, 4]  [3]         4
# 3     [3]     [1]         2

n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve))