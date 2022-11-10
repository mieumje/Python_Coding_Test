f = input()
arr = f.split('-')
tmp = []
for i in range(len(arr)):
  if '+' in arr[i]:
    sum = 0
    for j in arr[i].split('+'):
      sum += int(j)
    tmp.append(sum)
  else:
    tmp.append(int(arr[i]))
    
answer = tmp[0]
for i in range(1, len(tmp)):
  answer -= tmp[i]
  
print(answer)

# input                     answer
# 30-70-20+40-10+100+30-35  -275
# 55-50+40                  -35
# 10+20+30+40               100
# 00009-00009               0