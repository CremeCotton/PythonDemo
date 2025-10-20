# 创建数值列表

# 使用函数range()
for value in range(1,10):
    print(value)

# 使用range()创建数值列表
Numbers = list(range(1,9))
print(Numbers)

# 对列表进行简单计算
Test_num = list(range(1,9))
print(f'最小的数字是{min(Test_num)}')
print(f'最大的数字是{max(Test_num)}')
print(f'所有数字加一起的和是{sum(Test_num)}')