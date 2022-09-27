import math

def solution(fees, records):
  answer = []
  max_time = (23 * 60) + 59
  default_time, default_price, per_time, per_price = fees
  dict = {}
  acc = {}
  
  for record in records:
    time_record, number, in_out = record.split(' ')
    hh, mm = time_record.split(':')
    sum_time = int(hh) * 60 + int(mm)
    
    if in_out == 'IN':
      dict[number] = sum_time
    
    if in_out == 'OUT':
      prev = dict[number]
      del dict[number]
      try:
        acc[number] += sum_time - prev
      except:
        acc[number] = sum_time - prev
  
  for k, v in dict.items():
    
    try:
      acc[k] += max_time - v
    except:
      acc[k] = max_time - v
  
  acc = sorted(acc.items())
  
  for record in acc:
    _, v = record
    
    if v > default_time:
      over_time = v - default_time
      answer.append(default_price + math.ceil(over_time / per_time) * per_price)
    else:
      answer.append(default_price)
  return answer



# fees	                records	                                                                                                                                                      result
# [180, 5000, 10, 600]	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]	[14600, 34400, 5000]
# [120, 0, 60, 591]	    ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]	                                                                          [0, 591]
# [1, 461, 1, 10]	      ["00:00 1234 IN"]	                                                                                                                                            [14841]

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fees, records))

fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]
print(solution(fees, records))

fees = [1, 461, 1, 10]	
records = ["00:00 1234 IN"]
print(solution(fees, records))
