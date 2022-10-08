def getMaximumRemovals(order, source, target):
    # Write your code here
    answer = 0
    if source == target:
        return 0
    arr = []
    
    for i in source:
      arr.append(i)
      
    for i in order:
      arr[i - 1] = ''
      if len(''.join(arr)) < len(target):
        break
      print(''.join(arr))
      tmp = ''.join(arr)
      idx = 0
      for j in tmp:
        if idx >= len(target):
          break
        if j == target[idx]:
          idx += 1
      
      if idx < len(target):
        break
      if idx == len(target):
        answer += 1
      
    return answer
    
order = [1, 4, 2, 3, 5]
source = 'hkbdi'
target = 'kd'

print(getMaximumRemovals(order,source,target))
