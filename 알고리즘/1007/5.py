def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    # Write your code here
    arr = [[0] * len(g_from) for _ in range(len(g_to))]
    for i in range(len(g_from)):
      x, y = g_from[i], g_to[i]
      arr[x][y] = g_weight[i]
    print(arr)
    
g_nodes = 5
g_from = [1,2,3,4,5,3]
g_to = [2,3,4,5,1,5]
g_weight = [9,11,6,1,4,10]
x = 2
y = 3

print(minCostPath(g_nodes, g_from, g_to, g_weight, x, y))