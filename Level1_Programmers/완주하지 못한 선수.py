''' 
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요. 
'''
# 참가자 중에는 동명이인이 있을 수 있습니다.

def solution(participant, completion):
    answer = ""
    list = {}
    for i in participant:
        try : list[i] += 1
        except : list[i] = 1
    
    for i in completion:
        list[i] -= 1
     
    for i in list:
        if list[i] != 0:
            answer = i
    return answer

# 입출력 예
# participant	                                    completion	                                return
# ["leo", "kiki", "eden"]	                        ["eden", "kiki"]	                        "leo"
# ["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
# ["mislav", "stanko", "mislav", "ana"]	            ["stanko", "ana", "mislav"]	                "mislav"

participant	= ["mislav", "stanko", "mislav", "ana"]	
completion = ["stanko", "ana", "mislav"]	   

print(solution(participant, completion))