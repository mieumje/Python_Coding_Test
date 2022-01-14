"""
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return
"""
def solution(phone_book):
    phone_book.sort()
    l = len(phone_book)
    
    for i in range(1, l):
        if(phone_book[i].startswith(phone_book[i-1])):
            return False
    
    return True

# 입출력 예제
# phone_book	                    return
# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	            true
# ["12","123","1235","567","88"]	false

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))