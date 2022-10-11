def solution(survey, choices):
  answer = ''
  points = [None, 3, 2, 1, 0, 1, 2, 3]
  lists = {
    'R': 0,
    'T': 0,
    'C': 0,
    'F': 0,
    'J': 0,
    'M': 0,
    'A': 0,
    'N': 0
  }
  
  for i in range(len(survey)):
    positive, negative = survey[i][0], survey[i][1]
    if choices[i] == 4:
      continue
    elif choices[i] > 4:
      lists[negative] += points[choices[i]]
    else:
      lists[positive] += points[choices[i]]
  
  keys = list(lists)
  for i in range(0, 8, 2):
    if lists[keys[i]] == lists[keys[i + 1]]:
      answer += keys[i]
      continue
    answer += keys[i] if lists[keys[i]] > lists[keys[i + 1]] else keys[i + 1]
  
  return answer
  
# survey	                        choices	        result
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# ["TR", "RT", "TR"]	            [7, 1, 3]	      "RCJA"

survey = ["TR", "RT", "TR"]
choices = [7, 1, 3]

print(solution(survey, choices))