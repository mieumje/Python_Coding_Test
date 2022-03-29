def solution(n, computers):
    def dfs(start, n, computers, check):
        stack = [start]

        while(stack):
            curr = stack.pop()
            check[curr] = True

            for i in range(n):
                if not check[i] and computers[curr][i]:
                    stack.append(i)
        return

    answer = 0
    check = [False for _ in range(n)]

    for i in range(n):
        if not check[i]:
            dfs(i, n, computers, check)
            answer += 1

    return answer


# n	computers	                        return
# 3	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]	2
# 3	[[1, 1, 0], [1, 1, 1], [0, 1, 1]]	1
n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
