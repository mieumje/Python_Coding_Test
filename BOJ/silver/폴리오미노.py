Input = input()
answer = ''
tmp = ''

for i in Input:
  if i == '.' and len(tmp) == 0:
    answer += i
  elif i == '.' and len(tmp) > 0:
    if len(tmp) % 2 != 0:
      answer = -1
      break
    div, mod = divmod(len(tmp), 4)
    answer += ('AAAA' * div) + ('B' * mod) + '.'
    tmp = ''
  elif i == 'X':
    tmp += i

if tmp and len(tmp) % 2 != 0:
  answer = -1
else:
  div, mod = divmod(len(tmp), 4)
  answer += ('AAAA' * div) + ('B' * mod)

print(answer)