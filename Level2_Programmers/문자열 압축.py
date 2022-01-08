"""문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현"""
def solution(s):
    result = []
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s) // 2 + 1):
        cnt = 1                                     # 문자가 반복된 횟수
        tmpS = s[:i]                                # 반복될 문자
        result_str = ''                 
        for j in range(i, len(s), i):               # i 만큼 길이의 tmpS가 반복되는지 확인 
            if tmpS == s[j:j+i]:                    # tmpS 이후의 오는 문자가 tmpS와 같은지 확인
                cnt += 1                            # 문자가 반복된 횟수 ++
            else:                                   # tmpS 이후의 오는 문자가 tmpS와 다를 때,
                if cnt != 1:                        # 문자가 반복된 횟수가 1회 이상인 경우
                    result_str += str(cnt) + tmpS   # result_str += 반복된 횟수 + 반복된 문자
                else:                               # 문자가 반뵉된 횟수가 1회 이상이 아닌 경우
                    result_str += tmpS              # result_str += tmpS
                tmpS = s[j:j+i]                     # 반복된 문자를 더한 후 다음 반복될 문자
                cnt = 1                             # 문자가 반복된 횟수 초기화
        
        if cnt != 1:                                # 두번째 반복문 안에 있는 같은 조건문을 실행한 이유 : 마지막 반복 문자를 더하기 위함
            result_str += str(cnt) + tmpS
        else:
            result_str += tmpS
        
        result.append(len(result_str))              # 반복될 문자의 길이가 1 ~ (len(s) // 2 + 1) 인 경우의 결과를 저장

    answer = min(result)                            # 최종 답은 배열에 담긴 최솟값
    return answer
# 입출력 예
# s	                            result
# "aabbaccc"	                7
# "ababcdcdababcdcd"	        9
# "abcabcdede"	                8
# "abcabcabcabcdededededede"	14
# "xababcdcdababcdcd"	        17
"""
입출력 예에 대한 설명
입출력 예 #1

문자열을 1개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #2

문자열을 8개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #3

문자열을 3개 단위로 잘라 압축했을 때 가장 짧습니다.

입출력 예 #4

문자열을 2개 단위로 자르면 "abcabcabcabc6de" 가 됩니다.
문자열을 3개 단위로 자르면 "4abcdededededede" 가 됩니다.
문자열을 4개 단위로 자르면 "abcabcabcabc3dede" 가 됩니다.
문자열을 6개 단위로 자를 경우 "2abcabc2dedede"가 되며, 이때의 길이가 14로 가장 짧습니다.

입출력 예 #5

문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다.
따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
이 경우 어떻게 문자열을 잘라도 압축되지 않으므로 가장 짧은 길이는 17이 됩니다.
"""

s = "ababcdcdababcdcd"
print(solution(s))

