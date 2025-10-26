# 一个基础的IF演示
brand_list = ['bmw','audi','benz','toyota','honda']

# 检查是否在列表中
if 'porsche' in brand_list:
    print('在列表中')
else:
    print('不在列表中')

# 检查是否相等
if brand_list[0] == 'bmw':
    print('都是全小写')
else:
    print('不是全小写')

# 检查时忽略大小写
if brand_list[0].lower() == 'bmw':
    print('都是全小写')
else:
    print('不是全小写')

 # 检查是否不等
target_brand = 'bmw'
if target_brand != 'bmw':
    print('是小写')
else:
    print('是大写')

# 数值比较
age = 18
if age < 18:
    print('未成年')
elif age >= 18:
    print('成年')

# 检查多个条件，使用and
age = 20
name = 'Clay'
if age == 20 and name == 'Clay':
    print('恭喜晋级')
else:
    print('抱歉你被淘汰了')

# 检查多个条件，使用or
Math = 90
Physics = 80
if Math or Physics >= 80:
    print('恭喜通过')
else:
    print('继续努力')

# 检查特定值不在列表中
subjects = ['Chinese','Math','English']
target_subject = 'Pyshics'
if target_subject not in subjects:
    print('物理不在此列表中')

