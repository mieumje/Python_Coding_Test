def solution(w,h):
    answer = 1
    M = max(w,h)
    GCD = 0                             # w, h의 최대 공약수를 구함
    for i in range(1, M+1):
        if(w % i == 0 and h % i == 0):
            GCD = i                       # w, h의 최대공약수
    
    if(w == 0 or h == 0):               # w, h의 길이가 1cm인 경우 정답 = 0
        return 0
    if(w == h):                         # w, h의 길이가 같은 정사각형의 경우
        return (w * h) - w              # w * h 에서 w만큼 제거
    
    # 그 외의 경우 >> w * h를 최대 공약수 만큼 줄임                                        
    W = w // GCD                        # w / 최대 공약수
    H = h // GCD                        # h / 최대 공약수
                                        
    answer = w * h - (GCD * ((W - 1) + H))
    return answer

# 입출력 예
# W	H	result
# 8	12	80

# 입출력 예 설명
# 입출력 예 #1
# 가로가 8, 세로가 12인 직사각형을 대각선 방향으로 자르면 총 16개 정사각형을 사용할 수 없게 됩니다. 
# 원래 직사각형에서는 96개의 정사각형을 만들 수 있었으므로, 96 - 16 = 80 을 반환합니다.

W = 8
H = 12
print(solution(W,H))