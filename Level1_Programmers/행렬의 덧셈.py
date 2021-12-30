def solution(arr1, arr2):
    answer = []
    
    for i in range(0, len(arr1)):
        brr = []
        for j in range(0, len(arr1[i])):
            brr.append(arr1[i][j] + arr2[i][j])
        answer.append(brr)
        
    return answer

# arr1	        arr2	        return
# [[1,2],[2,3]]	[[3,4],[5,6]]	[[4,6],[7,9]]
# [[1],[2]]	    [[3],[4]]	    [[4],[6]]

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]

print(solution(arr1, arr2))