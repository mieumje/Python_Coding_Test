import statistics
import numpy

def solution(arr):
    answer = statistics.mean(arr)
    return answer

def solution2(arr):
    answer = numpy.mean(arr)
    return answer

def solution3(arr):
    ansewr = sum(arr) / len(arr)
    return ansewr

arr = [1,2,3,4]
print(solution(arr), solution2(arr), solution3(arr))