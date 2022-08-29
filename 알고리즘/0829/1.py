from unittest import result
from numpy import absolute


def solution(absolutes, signs):
    answer = 0;
    length = len(absolutes);
    for i in range(0, length):
      if signs[i] == True:
        answer += absolutes[i]
      else:
        answer += absolutes[i] * -1
    return answer


# absolutes   signs                 result
# [4,7,12]    [True, False, True]   9
# [1,2,3]     [False, False, True]  0

absolutes = [4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))