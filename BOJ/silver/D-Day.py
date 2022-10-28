import datetime


def solution():
  def max_diff():
    day = 0
    for i in range(yy, yy + 1000):
      if i % 400 == 0:
        day += 366
      elif i % 100 == 0:
        day += 365
      elif i % 4 == 0:
        day += 366
      else:
        day += 365
    return day
  d_days = 0

  yy, mm, dd = map(int, input().split())
  YY, MM, DD = map(int, input().split())
  today = datetime.date(yy, mm, dd)
  target = datetime.date(YY, MM, DD)
  
  d_days = (target - today).days
  
  answer = f'D-{d_days}' if d_days < max_diff() else 'gg'
  
  return answer

print(solution())