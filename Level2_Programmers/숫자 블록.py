def solution(begin, end):
  answer = []
  end_block = end // 2
  arr = [0] * (end + 1)

  for i in range(end_block, 0, -1):
    tmp = 2
    while True:
      if tmp * i > end: break
      
      if arr[tmp * i] == 0:
        arr[tmp * i] = i
      tmp += 1
  
  answer = arr[begin:end + 1]
  return answer

# begin	end	result
# 1	    10	[0, 1, 1, 2, 1, 3, 1, 4, 3, 5]

begin = 1
end = 11

print(solution(begin, end))

#       1  2  3  4  5  6  7  8  9  10 11 12 13 14 15
# init  0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 
#   1   0  1  1  1  1  1  1  1  1  1  1  1  1  1  1
#   2   0  1  1  2  1  2  1  2  1  2  1  2  1  2  1
#   3   0  1  1  2  1  3  1  2  3  2  1  3  1  2  1 
#   4   0  1  1  2  1  3  1  4  3  2  1  4  1  2  1
#   5   0  1  1  2  1  3  1  4  3  5  1  4  1  2  1
#   6   0  1  1  2  1  3  1  4  3  5  1  6  1  2  1