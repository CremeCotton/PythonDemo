# 遍历字典,也就是使用for循环输出
computer_brand = {
    'Lenovo':'联想',
    'Dell':'戴尔',
    'HP':'惠普',
    'H3C':'华三',
}

# 输出字典
for en_name,cn_name in computer_brand.items():
    print(f'{en_name}对应的中文名称是{cn_name}')

# 输出字典中的键
print('所有的英文名称如下:')
for en_name in computer_brand.keys():
    print(f'{en_name}')
# 输出字典中的值
print('所有的中文名称如下:')
for cn_name in computer_brand.values():
    print(f'{cn_name}')

# 按照特定顺序遍历字典的键
