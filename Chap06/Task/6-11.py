cities = {
    'Shanghai':{
        'country':'China',
        'population':'超千万级别',
        'fact':'魔都'
    },
    'London':{
        'country':'UK',
        'population':'超千万级别',
        'fact':'英国首都'
    },
    'Tokyo':{
        'country':'Japan',
        'population':'超千万级别',
        'fact':'日本首都'
    }
}
for city_name,city_description in cities.items():
    print(f'这个城市的名称是{city_name},这个城市是在{city_description['country']},人口规模时{city_description['population']},一个事实是{city_description['fact']}')