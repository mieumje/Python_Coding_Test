def solution(rows, columns, queries):
  answer = []
  arr = []
  index = 0
  
  for _ in range(rows):
    tmp = []
    for _ in range(columns):
      index += 1
      tmp.append(index)
    arr.append(tmp)
  
  for query in queries:
    row1, col1, row2, col2 = query[0] - 1, query[1] - 1, query[2] - 1, query[3] - 1 
    tmp = []
    for i in range(col1, col2 + 1):
      tmp.append(arr[row1][i])
    for i in range(row1 + 1, row2 + 1):
      tmp.append(arr[i][col2])
    for i in range(col2 - 1, col1 - 1, -1):
      tmp.append(arr[row2][i])
    for i in range(row2 - 1, row1, - 1):
      tmp.append(arr[i][col1])
    
    tmp.insert(0, tmp.pop())
    answer.append(min(tmp))
    
    for i in range(col1, col2 + 1):
      arr[row1][i] = tmp.pop(0)
    for i in range(row1 + 1, row2 + 1):
      arr[i][col2] = tmp.pop(0)
    for i in range(col2 - 1, col1 - 1, -1):
      arr[row2][i] = tmp.pop(0)
    for i in range(row2 - 1, row1, - 1):
      arr[i][col1] = tmp.pop(0)

  return answer

# rows	columns	queries	                                  result
# 6	    6	      [[2,2,5,4],[3,3,6,6],[5,1,6,3]]	          [8, 10, 25]
# 3	    3	      [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	[1, 1, 5, 3]
# 100	  97	    [[1,1,100,97]]	                          [1]

rows = 100
columns = 97
queries = [[1,1,100,97]]
print(solution(rows, columns, queries))