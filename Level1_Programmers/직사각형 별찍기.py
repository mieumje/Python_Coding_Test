a, b = map(int, input().strip().split(' '))
for i in range(0, b):
    str = ""
    for j in range(0, a):
        str += "*"
    print(str)