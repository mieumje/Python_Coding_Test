def solution(s):
  tmp = list(map(int, s.split(' ')))
  answer = [str(min(tmp)), str(max(tmp))]
  answer = ' '.join(answer)
    
  return answer


# s	              return
# "1 2 3 4"	      "1 4"
# "-1 -2 -3 -4"	  "-4 -1"
# "-1 -1"	        "-1 -1"