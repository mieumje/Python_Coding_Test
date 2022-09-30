def solution(skill, skill_trees):
  answer = len(skill_trees)
  
  for skill_tree in skill_trees:
    cnt = 0
    for sk in skill_tree:
      if sk in skill:
        if sk != skill[cnt]:
          answer -= 1
          break
        else:
          cnt += 1
          continue

  return answer

# skill	skill_trees	                      return
# "CBD"	["BACDE", "CBADF", "AECB", "BDA"]	2

print(solution(skill='CBD', skill_trees=["BACDE", "CBADF", "AECB", "BDA"]))