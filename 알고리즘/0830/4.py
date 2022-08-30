def solution(n, k, cmd):
    global table, current
    current = k
    table = {}
    stack = []
    answer = ''
    
    for i in range(n):
      table[i] = 'O'
    
    last_idx = len(table) - 1
    
    for i in cmd:
      command = i.split(' ')
      
      if command[0] == 'D':
        idx = int(command[1])
        for i in range(idx):
          current = current + 1
          if current > last_idx:
            current = 0
          while True:
            if table[current] == 'O':
              break
            else:
              current = current + 1
              if current > last_idx:
                current = 0
          
      if command[0] == 'U':
        idx = int(command[1])
        # current = (current + idx) % (n - 1)
        for i in range(idx):
          current = current - 1
          if current < 0:
            current = last_idx
          while True:
            if table[current] == 'O':
              break
            else:
              current = current - 1
              if current < 0:
                current = last_idx
        
      if command[0] == 'C':
        stack.append([current])
        # print('delete', current)
        table[current] = 'X'
        
        while True:
          if current == last_idx:
            current = current - 1
          else:
            current = current + 1
            
          if table[current] == 'O':
            break
          
      if command[0] == 'Z':
        restore_idx = stack.pop()[0]
        # print('restore index is ', restore_idx)

        table[restore_idx] = 'O'
    
    for i in table:
      answer = answer + table[i]
      
    return answer
    
  
# n   k   cmd                                                                 result
# 8   2   ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]               "OOOOXOOO"
# 8   2   ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]   "OOXOXOOO"

n = 8
k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(n, k, cmd))
