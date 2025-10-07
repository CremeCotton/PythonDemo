Travel_List = ['Beijing','Shanghai','LA','Wuhan']
# 先正常输出一遍
print(f'我想去的城市如下:{Travel_List}')
# 进行临时排序
print(f'临时排序之后为:{sorted(Travel_List)}')
# 再次打印列表检查是否有改变
print(f'检查列表是否有改变:{Travel_List}')
# 先临时排序然后再反转
Temp_List = sorted(Travel_List)
print(f'再次临时排序后结果为{Temp_List}')
# 剩下的题目逻辑混乱，到此结束