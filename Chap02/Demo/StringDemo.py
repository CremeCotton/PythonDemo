# 关于Python处理字符串的相关演示

# 使输出的内容包括了引号
message = 'target school is "Caltech"'
print(f'he send me a message,the contect is his {message}')

# 修改字符串的大小写
my_name = 'Jason Hayes'
# 全部改为大写
print(f'将名称全部改为大写之后是:{my_name.upper()}')
# 全部改为小写
print(f'将名称全部噶为小写之后是:{my_name.lower()}')

# 将首字母全部改为大写
team_name = 'seal team'
print(f'将首字母全部改为大写后是:{team_name.title()}')

# 合并字符串
first_name = 'Clay'
last_name = 'Spenser'
full_name = first_name + last_name
print(f'合并后的全名是{first_name} {last_name}')

# 使用制表符来换行或者添加空白
print('此品牌的信息如下，名称是\t奥迪，详情如下:\n国家:德国')

# 删除空白
travel_city = ' hangzhou '
# 先将内容输出一遍
print(f'旅游城市有:{travel_city}')
# 去掉前面的空白
print(f'旅游城市有:{travel_city.lstrip()}')
# 去掉后面的空白
print(f'旅游城市有:{travel_city.rstrip()}')

# 适当的时候需要将数据的类型转换一下
age = 27
name = '张三'
# 将age的类型从数字改为字符串，然后一并输出
print(f'大家好我叫{name},今年{str(age)}岁')