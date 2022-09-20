def solution(S, pattern):
  answer = 0
  length = len(pattern)
  pattern = ''.join(sorted(pattern))

  for i in range(0, len(S) - length + 1):
    split_word = S[i:i+length]
    
    if ''.join(sorted(split_word)) ==  pattern:
      answer += 1
    
  return answer

# S                       pattern       result
# "tegsornamwaresomran"   "ransom"      2
# "wreawerewa"            "ware"        4
# "ababababababa"         "aabba"       5
# "abcde"                 "edcba"       1
# "aabbccddee"            "abcde"       0
# "aaaaaa"                "a"           6

S = "aaaaaa"  
pattern = "a" 

print(solution(S, pattern))