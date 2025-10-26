# 一个基础的字典演示
my_info = {
    'name':'Clay'
}
# 输出信息
print(f'我的名称是{my_info["name"]}')

# 添加信息
my_info['age'] = 20
print(f'我今年已满{my_info["age"]}岁')

# 先创建一个空的字典，然后再添加信息
stu_info = {}
stu_info['name'] = 'Jason'
stu_info['age'] = 30
print(f'此学生的姓名是{stu_info["name"]}')
print(f'此学生的年龄是{stu_info['age']}')

# 修改字典中的值
stu_info['age'] = 32
print(f'此学生的年龄需要修改，正确是今年{stu_info["age"]}岁')

# 删除键值对 删除年龄这一项信息
del stu_info['age']
print(stu_info)