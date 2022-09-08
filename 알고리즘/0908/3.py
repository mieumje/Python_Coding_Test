def solution(numbers):
    answer = []
    for i in numbers:
      bin_number = list('0' + bin(i)[2:])
      
      idx = ''.join(bin_number).rfind('0')
      print(i, bin_number, idx)
      bin_number[idx] = '1'
      
      if i % 2 == 1:
        bin_number[idx + 1] = '0'
        
      answer.append(int(''.join(bin_number), 2))
      
    return answer

numbers = [2, 4, 7]
print(solution(numbers))

# 가장 오른쪽에 있는 0을 1로 바꾼다 => 0의 위치 = idx
# 홀수 인 경우 idx + 1을 0으로 바꾼다
# 해당 2진수를 10진수로 변경