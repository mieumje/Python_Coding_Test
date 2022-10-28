x = int(input())
stick = 64
cnt = 0

while x > 0:
  if stick > x:
    stick /= 2
  else:
    cnt += 1
    x -= stick
print(cnt)