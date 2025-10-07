# 对列表进行排序

# 进行排序 永久的
Country_List = ['China','Japan','America','Singapore']
Country_List.sort()
print(Country_List)

# 临时排序，再次输出顺序不会改变
Programming_List = ['Python','C++','Go','Rust']
Temp_List = sorted(Programming_List)
print(Temp_List)
print(Programming_List)

# 反转打印列表
food_list = ['humbuger','hot dog','pizza']
food_list.reverse()
print(food_list)

# 列表的长度
Main_Subject = ['Chinese','Math','English']
print(f'主课总计有{len(Main_Subject)}门,分别是以下科目:')
for subject in Main_Subject:
    print(subject)