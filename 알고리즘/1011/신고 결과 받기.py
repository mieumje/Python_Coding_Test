def solution(id_list, report, k):
    answer = [0] * len(id_list)
    counts = {}
    records = {}
    for id in id_list:
      counts[id] = 0
      records[id] = []
    
    for r in report:
      reporter, subject = r.split(' ')
      if subject not in records[reporter]:
        records[reporter].append(subject)
        counts[subject] += 1

    idx = 0
    for key in records:
      for s in records[key]:
        if counts[s] >= k:
          answer[idx] += 1
      idx += 1
    
    return answer
  
  
# id_list	                            report	                                                            k	result
# ["muzi", "frodo", "apeach", "neo"]	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]	2	[2,1,1,0]
# ["con", "ryan"]	                    ["ryan con", "ryan con", "ryan con", "ryan con"]	                  3	[0,0]

id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]	 
k = 3

print(solution(id_list, report, k))