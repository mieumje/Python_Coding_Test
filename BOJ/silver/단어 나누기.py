data = input()
length = len(data)
arr = []

for i in range(1, length - 1):
  for j in range(i + 1, length):
    a = data[:i] 
    b = data[i:j] 
    c = data[j:]
    tmp = a[::-1] + b[::-1] + c[::-1]
    if not len(arr):
      arr.append(tmp)
      continue
    if arr[0] > tmp:
      arr[0] = tmp

print(arr[0])