def solution(n, k, cmd):
    current = k
    table = { i:[i - 1, i + 1] for i in range(n) }
    stack = []
    answer = ['O'] * n
    
    table[0] = [None, 1]
    table[n - 1] = [n - 2, None]
    
    
    for i in cmd:
      if len(i) > 1:
        command, idx = i.split(' ')
        idx = int(idx)
        
        if command == 'D':
          for _ in range(idx):
            current = table[current][1]
        else:
          for _ in range(idx):
            current = table[current][0]
      else:
        if i == 'C':
          answer[current] = 'X'
          prev, next = table[current]
          stack.append([prev, current, next])
          
          if next == None:
            current = table[current][0]
          else:
            current = table[current][1]
          
          if prev == None:
            table[next][0] = None
          elif next == None:
            table[prev][1] = None
          else:
            table[prev][1] = next
            table[next][0] = prev
            
        if i == 'Z':
          prev, now, next = stack.pop()
          answer[now] = 'O'
          
          if prev == None:
            table[next][0] = now
          elif next == None:
            table[prev][1] = now
          else:
            table[prev][1] = now
            table[next][0] = now
      print(table)
        
    
    return "".join(answer)
    
  
# n   k   cmd                                                                 result
# 8   2   ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]               "OOOOXOOO"
# 8   2   ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]   "OOXOXOOO"

n = 8
k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]

print(solution(n, k, cmd))
