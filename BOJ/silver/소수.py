A, B, N = map(int, input().split())
answer = 0
for _ in range(N):
  A = (A % B) * 10
  answer = A // B
print(answer)

# A   B   N       result
# 25  7   4       4
# 11  14  10000   7
# 1   4   7       0
# 1   3   1000000 3