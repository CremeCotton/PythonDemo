# 对列表进行增删改查
cars = ['Audi','BMW','Benz','Toyota','Honda']
# 先输出一遍
print(f'品牌如下:\n{cars}')

# 将日系品牌改为欧美品牌  修改
print('将最后面的两个汽车品牌更换为欧洲的')
cars[-2] = 'GME'
cars[-1] = 'Porsche'
print(f'最后输出结果为:\n{cars}')

# 向列表添加品牌 在尾部添加
cars.append('BYD')
# 输出
print(f'添加BYD品牌之后结果为:\n{cars}')
# 向列表添加品牌 在列表中间添加
cars.insert(1,'Subaru')
print(f'将Subare这个品牌添加到第二的位置后结果为:\n{cars}')

# 删除列表中的元素
# 使用del来删除元素
del cars[0]
print(f'删除第一个品牌之后结果为:\n{cars}')

# 使用pop来删除元素 删除之前可以调取出来说明一下
pop_car = cars.pop(0)
print(f'准备删除的品牌是{pop_car}')
print(f'删除之后的汽车品牌名单如下:{cars}')
# 可以用来调取任意一个位置的列表元素,比如是第三个元素
second_pop_car = cars.pop(-1)
print(f'准备删除的第二个品牌是{second_pop_car}')
print(f'删除之后的汽车品牌名单如下:{cars}')

# 根据值来删除元素
# 使用remove() 从列表中删除元素时，也可接着使用它的值。
# 删除GME这个品牌
target_brand = 'GME'
reason = '非TOP品牌'
cars.remove(target_brand)
print(f'被删除的品牌是{target_brand},原因是{reason}')
print(f'最新的品牌列表如下:{cars}')