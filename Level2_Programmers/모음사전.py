def solution(word):
  cnt = 0
  dict = {}
  lists = ['A', 'E', 'I', 'O', 'U']
  
  def dfs(s, lists):
    nonlocal cnt
    for i in lists:
      if len(s) == 5:
        return
      tmp = s + i
      cnt += 1
      dict[tmp] = cnt
      
      if tmp == word:
        break
      dfs(tmp, lists)
      
  dfs('', lists)  
  
  return dict[word]

# word	  result
# "AAAAE"	6
# "AAAE"	10
# "I"	    1563
# "EIO"	  1189

print(solution(word='AAAAE'))
print(solution(word='AAAE'))
print(solution(word='I'))
print(solution(word='EIO'))
print(solution(word='A'))
print(solution(word='E'))
print(solution(word='I'))
print(solution(word='O'))
print(solution(word='U'))



