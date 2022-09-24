def solution(clothes):
  answer = 1
  list = {}
  for cloth in clothes:
    [_, category] = cloth
    try:
      list[category] += 1
    except:
      list[category] = 1
  for _, v in list.items():
    answer *= (v + 1)
    
  return answer - 1

# clothes	                                                                                    return
# [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]	5
# [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	            3

clothes = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]	

print(solution(clothes))
