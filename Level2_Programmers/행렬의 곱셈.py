def solution(arr1, arr2):
  answer = []
  
  for x in range(len(arr1)):
    arr = []
    for y in range(len(arr2[0])):
      tmp = 0
      for z in range(len(arr1[0])):
        tmp += arr1[x][z] * arr2[z][y]
      arr.append(tmp)
    answer.append(arr)
        
  return answer

# arr1	                            arr2	                            return
# [[1, 4], [3, 2], [4, 1]]	        [[3, 3], [3, 3]]	                [[15, 15], [15, 15], [15, 15]]
# [[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]

print(solution(arr1, arr2))