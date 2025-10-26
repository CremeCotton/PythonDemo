# 检查两个字符串是否相等或者不相等
first_str = 'hello'
second_str = 'hello'
print(f'上面两个字符串是否相等:{first_str==second_str}')

# 使用lower()对比字符串
first_str = 'hello'
second_str = 'Hello'
if first_str == second_str.lower():
    print('忽略大小写之后是一样的')
else:
    print('忽略大小写之后是不一样的')

# 第三项直接跳过

# 使用and和or进行测试
Chinese = 90
Math = 100
if Chinese and Math >= 90:
    print('两门科目都及格了')
else:
    print('有一门的成绩有问题')
if Chinese or Math >= 100:
    print('有一科及格了')
else:
    print('搞砸了')

# 检查特定值在/不在列表中
brand_list = ['Audi','Porsche','BMW','Honda','Toyota']
if 'Audi' in brand_list:
    print('奥迪确实在列表中')
if 'GMC' not in brand_list:
    print('GMC确实不在列表中')