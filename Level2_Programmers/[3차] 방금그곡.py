import math

def solution(m, musicinfos):
  answer = ''
  arr = []
  idx = 0
  
  def replace_codes(music):
    codes = {'C#': 'c', 'D#' : 'd', 'F#': 'f', 'G#': 'g', 'A#': 'a'}
    for code in codes:
      music = music.replace(code, codes[code])
    return music
  
  m = replace_codes(m)
  
  for music_info in musicinfos:
    infos = music_info.split(',')
    hh, mm = infos[0].split(':')
    HH, MM = infos[1].split(':')
    music_title = infos[2]
    music_code = replace_codes(infos[3])
    music_play_time = (int(HH) * 60) + int(MM) - (int(hh) * 60) + int(mm)
    music_code *= math.ceil(music_play_time / len(music_code))
    
    if m not in music_code:
      continue
    idx += 1
    arr.append([idx, music_title, music_play_time])
  
  if not arr:
    return '(None)'
  
  arr = sorted(arr, key = lambda x : (-x[2], x[0]))
  
  answer = arr[0][1]
  
  return answer

# m	                  musicinfos	                                                answer
# "ABCDEFG"	          ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]	  "HELLO"
# "CC#BCC#BCC#BCC#B"	["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]	  "FOO"
# "ABC"	              ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]	"WORLD"

m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]

print(solution(m, musicinfos))