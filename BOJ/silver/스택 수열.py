n = int(input())

stack = []
answer = []
current = 1

for i in range(n):
  number = int(input())

  while current <= number:
    stack.append(current)
    answer.append('+')
    current += 1

  if stack[-1] != number:
    print('NO')
    break
  else:
    stack.pop()
    answer.append('-')

if i == n - 1:
  for item in answer:
    print(item)