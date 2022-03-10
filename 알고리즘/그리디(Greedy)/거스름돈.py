n = int(input())
answer = 0

coins = [500, 100, 50, 10]

for coin in coins:
    answer += n // coin
    n = n % coin

print(answer)
