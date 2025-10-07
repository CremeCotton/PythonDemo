# 3-4
member_list = ['Jason','Clay','Ray','Stella','Sonny']
for member in member_list:
    print(f'欢迎{member}一起干饭')
# 3-5
pop_member = member_list[1]
print(f'{member_list[2]}因为有任务无法出席晚宴')
# 将Ray的席位让给Bill
member_list[2] = 'Bill'
for member in member_list:
    print(f'欢迎{member}一起干饭')
# 3-6
print('我找到了一个更大的桌子')

# 使用insert添加到头部
member_list.insert(0,'Boss')
# 输出结果
print('添加Boss到第一位,输出名单')
print(f'晚宴名单如下:\n{member_list}')

# 使用insert添加到中间位置
member_list.insert(2,'Robin')
# 输出结果
print(f'添加Robin到列表中部位置\n{member_list}')

# 使用append添加嘉宾
member_list.append('Lora')
# 输出结果
print(f'添加Lora到最新的名单如下:\n{member_list}')

for mem in member_list:
    print(f'{mem}欢迎参加最后的晚宴')

# 3-7
print('由于一些变故，只能邀请两位参加')
member_list.pop()
member_list.pop()
member_list.pop()
member_list.pop()
member_list.pop()
member_list.pop()
print(f'两位嘉宾是{member_list}')
for final_list in member_list:
    print(f'恭喜{final_list},你们还在受邀列表中')
del member_list[0]
del member_list[0]
# 此处用来判断列表为空
if not member_list:
    print('此列表为空')

