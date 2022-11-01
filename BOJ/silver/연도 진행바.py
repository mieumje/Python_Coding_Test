Input = input()
tmp = Input.split(',')
MM, DD = tmp[0].split(' ')
year_time = tmp[1].lstrip().split(' ')
YY = year_time[0]
hh, mm = year_time[1].split(':')
times = [525600, 527040]

months = {
   'January': [0, 0],
   'February': [31, 31],
   'March': [59, 60],
   'April': [90, 91], 
   'May': [120, 121], 
   'June': [151, 152], 
   'July': [181, 182], 
   'August': [212, 213], 
   'September': [243, 244], 
   'October': [273, 274],
   'November': [304, 305], 
   'December': [334, 335],
}

sum = 0
flag = False

if int(YY) % 400 == 0 or int(YY) % 4 == 0 and int(YY) % 100 != 0:
  flag = True

sum += months[MM][0] if not flag else months[MM][1]
sum -= 1
sum += int(DD)
time = (sum * 24 * 60) + int(hh) * 60 + int(mm)
answer = (time / times[0]) * 100 if not flag else (time / times[1]) * 100
print(answer)