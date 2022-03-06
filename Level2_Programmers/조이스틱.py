def solution(name):
    answer = 0
    tmp = [min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
           for char in name]

    cur = 0
    while True:
        answer += tmp[cur]
        tmp[cur] = 0
        if sum(tmp) == 0:
            break

        left, right = 1, 1
        while tmp[cur - left] == 0:
            left += 1
        while tmp[cur + right] == 0:
            right += 1

        answer += left if left < right else right
        cur += -left if left < right else right

    return answer


# 입출력 예
# name	    return
# "JEROEN"	56
# "JAN"	    23
name = "JEROEN"
print(solution(name))
