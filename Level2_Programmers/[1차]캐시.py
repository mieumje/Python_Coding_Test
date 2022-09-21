def solution(cacheSize, cities):
  answer = 0
  cache_hit = 1
  cache_miss = 5
  
  if cacheSize == 0:
    answer = len(cities) * 5
    return answer
  
  for i in range(len(cities)):
    cities[i] = cities[i].lower()
    
  cache = []
  
  for city in cities:
    if city not in cache:
      if len(cache) < cacheSize:
        cache.append(city)
        answer += cache_miss
      else:
        cache.pop(0)
        cache.append(city)
        answer += cache_miss
    else:
      cache.pop(cache.index(city))
      cache.append(city)
      answer += cache_hit
        
  return answer

# cacheSize	도시이름(cities)	                                                                                                  실행시간
# 3	        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	                         50
# 3	        ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]	                                 21
# 2	        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	 60
# 5	        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]	 52
# 2	        ["Jeju", "Pangyo", "NewYork", "newyork"]	                                                                         16
# 0	        ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]	                                                                     25

cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

print(solution(cacheSize, cities))

print(solution(cacheSize=0, cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))