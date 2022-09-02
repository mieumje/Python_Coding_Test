def solution(lottos, win_nums):
    answer = []
    
    ranks = {
      6: 1,
      5: 2,
      4: 3,
      3: 4,
      2: 5,
      1: 6,
      0: 6,
    }
    
    correct_cnt = 0
    zero_cnt = 0
    
    for i in lottos:
      if i in win_nums:
        correct_cnt = correct_cnt + 1
      
      if i == 0:
        zero_cnt = zero_cnt + 1
    
    answer.append(ranks[correct_cnt + zero_cnt])
    answer.append(ranks[correct_cnt])
    
    return answer
  
# lottos            win_nums            result
# [44,1,0,0,31,25]  [31,10,45,1,6,19]   [3,5]
# [0,0,0,0,0,0]     [38,19,20,40,15,25] [1,6]
# [45,4,35,20,3,9]  [20,9,3,45,4,35]    [1,1]


lottos = [45,4,35,20,3,9]
win_nums = [20,9,3,45,4,35]

print(solution(lottos, win_nums))