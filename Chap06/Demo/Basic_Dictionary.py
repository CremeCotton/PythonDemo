# 一个基础的字典演示
person_info = {
    'name':'Clay',
    'age':25,
}

# 访问字典中的值
print(f'大家好我叫{person_info["name"]}')

# 添加键值对
person_info['city'] = 'New York'
print(f'我工作生活在{person_info["city"]}')

# 创建一个空字典然后添加键值对
# 创建一个空字典
stu_info = {}
stu_info['name'] = 'Tony'
stu_info['level'] = 'High School'
print(stu_info)
# 修改字典中的值
stu_info['name'] = 'Jerry'
print(stu_info)

# 删除键值对
del stu_info['level']
print(f'最新的学生信息如下:{stu_info}')

# 遍历字典
airport_info = {
    'HGH':'杭州萧山国际机场',
    'SHA':'上海虹桥国际机场',
    'PEK':'北京首都国际机场',
    'HKG':'香港国际机场'
}
# 完整遍历
for en_name,cn_name in airport_info.items():
    print(f'{en_name}对应的中文名称是{cn_name}')

# 遍历字典中的键 
for en_name in airport_info.keys():
    print(en_name)

# 遍历字典中的值
for cn_name in airport_info.values():
    print(cn_name)