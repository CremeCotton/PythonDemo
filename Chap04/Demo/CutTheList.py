# 使用列表的一部分
foods = ['egg','hot dog','bread','noodle','fresh fish']
print(f'最前面的三个选项是:{foods[:3]}')
print(f'最后的两个选项是:{foods[-2:]}')

# 遍历第一个切片
print('前三选项是')
for food in foods[:3]:
    print(f'{food}')

# 遍历最后面的两个选项
print('最后的两个选项是')
for food in foods[-2:]:
    print(f'{food}')