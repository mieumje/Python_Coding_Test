def solution(pixels):
  answer = ''
  length = len(pixels[0])
  result_length = length // 3
  dict = {
    '111101101101111': '0',
    '110010010010111': '1',
    '111001111100111': '2',
    '111001111001111': '3',
    '101101111001001': '4',
    '111100111001111': '5',
    '111100111101111': '6',
    '111101001001001': '7',
    '111101111101111': '8',
    '111101111001111': '9'
  }
  
  arr = ['' for _ in range(result_length + 1)]
  
  for pixel in pixels:
    cnt = 0
    data = ''
    idx = 1
    for i in pixel:
      cnt += 1
      data += i
      
      if cnt == 3:
        arr[idx] += data
        cnt = 0
        data = ''
        idx += 1    
  
  for i in range(1, len(arr)):
    answer += dict[arr[i]]
  
  return answer

# pixels                                    result
# ["111111111111111111111111110111111111",  
#  "001101001101101100101101010101001100", 
#  "111101111101101111101111010111111111", 
#  "100101100101101101101001010101001001", 
#  "111111111111111111111111111111111111"]  "202006091835"
# ["110111101111111111110111", 
#  "010101101100101101010100", 
#  "010111111111101111010111", 
#  "010001001001101101010001", 
#  "111111001111111111111111"]              "19450815"
# ["111110111101111101111101", 
#  "100010101101001101100101", 
#  "111010111111111111111111", 
#  "001010101001100001001001", 
#  "111111111001111001111001"]              "51842454"
pixels = ["111110111101111101111101", 
 "100010101101001101100101", 
 "111010111111111111111111", 
 "001010101001100001001001", 
 "111111111001111001111001"]  

print(solution(pixels))