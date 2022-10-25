from itertools import combinations


def solution(relation):
  row = len(relation)
  col = len(relation[0])
  flag = False
  combis = []
  uniques = []
  
  for i in range(1, col + 1):
    coms = combinations(range(col), i)
    combis.extend(coms)
  
  for combi in combis:
    tmp = [''] * row
    for c in combi:
      idx = 0
      for item in relation:
        tmp[idx] += item[c]
        idx += 1
    # tmp = [item[key] for key in combi for item in relation]
    print(tmp)
    if row == len(set(tmp)):
      flag = True
      for unique in uniques:
        if set(unique) & set(combi):
          flag = False
          break
      
      if flag:
        uniques.append(combi)
  print(uniques)
  return len(uniques)

# relation	                        result
# [
#   ["100","ryan","music","2"],
#   ["200","apeach","math","2"],
#   ["300","tube","computer","3"],
#   ["400","con","computer","4"],
#   ["500","muzi","music","3"],
#   ["600","apeach","music","2"]]	  2

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]

print(solution(relation))