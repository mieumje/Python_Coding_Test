from bisect import bisect_left

def getMinimumHealth(initial_players, new_players, rank):
    # Write your code here
    answer = 0
    initial_players.sort()
    answer += initial_players[-rank]
    
    for m in new_players:
        idx = bisect_left(initial_players, m)
        initial_players.insert(idx, m)
        answer += initial_players[-rank]

    return answer

initial_players = [1, 2, 5]
new_players = [2, 5, 4]
rank = 2

print(getMinimumHealth(initial_players, new_players, rank))

print(bisect_left(initial_players, 2))
initial_players.insert(bisect_left(initial_players, 2), 2)
print(initial_players)