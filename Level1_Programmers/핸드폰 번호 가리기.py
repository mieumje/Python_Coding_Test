#전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴
def solution(phone_number):
    answer = ''
    length = len(phone_number)
    if(length == 4):
        return phone_number
    last_nums = phone_number[-4:]
    for i in range(0, length - 4):
        answer += "*"
    answer += last_nums
        
    return answer

# phone_number	return
# "01033334444"	"*******4444"
# "027778888"	"*****8888"