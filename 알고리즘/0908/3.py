def solution(numbers):
    answer = []
    for i in numbers:
      compare_number = i
      while True:
        xor_number = bin(i ^ compare_number)
        bin_number = xor_number.split('b')
        cnt = bin_number[1].count('1')
        if cnt == 1 or cnt == 2:
          answer.append(compare_number)
          break
        else:
          compare_number = compare_number + 1
    return answer

# print(bin(7))
# print('----')
# print(bin(7 ^ 8), bin(7 ^ 8).split('0b'))
# print(bin(7 ^ 9), bin(7 ^ 8).split('0b'))
# print(bin(7 ^ 10), bin(7 ^ 8).split('0b'))
# print(bin(7 ^ 11), bin(7 ^ 8).split('0b'))
# print(bin(7 ^ 12), bin(7 ^ 8).split('0b'))
# print(bin(7 ^ 13), bin(7 ^ 8).split('0b'))

# tmp = bin(7 ^ 13)
# for i in tmp:
#   print(i)
  
# arr = tmp.split('b')

# print(arr[1], arr[1].count('1'))

# numbers   result
# [2, 7]    [3, 11]
numbers = [2, 7]
print(solution(numbers))