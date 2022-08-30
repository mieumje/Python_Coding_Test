def solution(word):
    global idx
    answer = 0
    idx = 0
    
    arr = ['A', 'E', 'I', 'O', 'U']
    # words = []
    words = {}
    
    def combine_word(n, str):
      global idx
      if n == 5:
        return
      
      for i in range(len(arr)):
        next_word = str + arr[i]
        idx = idx + 1
        # words.append(next_word)
        words[next_word] = idx
        combine_word(n + 1, next_word)
    
    combine_word(0, '')
    
    answer = words[word]
      
    return answer
  
  
word = 'AAAAE'

print(solution(word))