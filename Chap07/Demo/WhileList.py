# 未去过的城市
unvisited_cities = ['London', 'New York', 'Sydney', 'Tokyo']
# 已去过的城市
visited_cities = []

while unvisited_cities:
    current_city = unvisited_cities.pop()
    print(f'刚去过的城市: {current_city}')
    visited_cities.append(current_city)

print('\n已去过的城市列表:')
for city in visited_cities:
    print(city)

