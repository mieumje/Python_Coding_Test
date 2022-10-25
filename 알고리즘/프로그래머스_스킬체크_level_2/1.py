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
    tmp = [tuple([item[key] for key in combi]) for item in relation]
    
    if row == len(set(tmp)):
      flag = True
      for unique in uniques:
        if set(unique).issubset(set(combi)):
          flag = False
          break
      
      if flag:
        uniques.append(combi)
  
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