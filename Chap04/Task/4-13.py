# 自助餐
food_list = ('热干面','三鲜豆皮','莲藕排骨汤','东坡肉','炒饭')

# 循环输出
for food in food_list:
    print(food)

# 尝试修改，失败
# food_list[-1] = '深海黄鱼'
# print(food_list[-1])

# 尝试替换，只能重新声明
food_list = ('热干面','三鲜豆皮','莲藕排骨汤','蛋酒','爆炒鳝鱼')
for food in food_list:
    print(food)