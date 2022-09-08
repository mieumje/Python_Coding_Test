def solution(s):
    answer = []
    target = '110'
    for i in s:
      tmp = i.split('110')
      tmp_str = ''
      if len(tmp[1]) == 0:
        tmp_str = tmp[0]
      else:
        tmp_str = ''.join(tmp)
      print(tmp_str)
    return answer
  

# s                                   result
# ['1110', '100111100', '0111111010'] ['1101', '100110110', '0110110111']

s = ['1110', '100111100', '0111111010']
print(solution(s))
