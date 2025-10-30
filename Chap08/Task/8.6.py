# 传递两个参数
def city_relation(city,country):
    info = f'{city}, {country}'
    return info.title()
sh = city_relation("上海","中国")
print(sh)