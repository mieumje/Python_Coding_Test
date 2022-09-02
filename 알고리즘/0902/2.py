def solution(numbers, hand):
    answer = ''
    left_hand = 10
    left_distance = 0
    right_hand = 12
    right_distance = 0

    for i in range(len(numbers)):
      if numbers[i] == 0:
        numbers[i] = 11
    
    def calc_dist(current, target):
      dist = 0
      dist_abs = abs(current - target)
      mod = dist_abs % 3
      n = dist_abs // 3
      
      dist = mod + n
      return dist
    
    for i in numbers:
      if i == 1 or i == 4 or i == 7:
        answer += 'L'
        left_hand = i
      if i == 3 or i == 6 or i == 9:
        answer += 'R'
        right_hand = i
      if i == 2 or i == 5 or i == 8 or i == 11:
        left_distance = calc_dist(left_hand, i)
        right_distance = calc_dist(right_hand, i)
        
        if len(answer) == 4:
          print('dist calc here')
          print(left_hand, left_distance)
          print(right_hand, right_distance)
          print('------')
        
        if left_distance < right_distance:
          answer += 'L'
          left_hand = i
        elif right_distance < left_distance:
          answer += 'R'
          right_hand = i
        elif left_distance == right_distance:
          answer += 'L' if hand == 'left' else 'R'
          left_hand = left_hand if hand == 'right' else i
          right_hand = right_hand if hand == 'left' else i
      print(i, answer, left_hand, right_hand)
    return answer
  


# numbers                 hand      result
# [1,3,4,5,8,2,1,4,5,9,5] "right"   "LRLLLRLLRRL"
# [7,0,8,2,8,3,1,5,7,6,2] "left"    "LRLLRRLLLRR"
# [1,2,3,4,5,6,7,8,9,0]   "right"   "LLRLLRLLRL"

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

# result = 'LRLLRRLLLRR'

print(solution(numbers, hand))