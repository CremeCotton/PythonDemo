# 元组
box_info = (20,10,30)
# 使用for循环遍历输出一遍
for len in box_info:
    print(len)
# 单独说明
print(f'盒子的长度是{box_info[0]}cm')
print(f'盒子的宽度是{box_info[1]}cm')
print(f'盒子的高度是{box_info[2]}cm')

# 修改元组变量，只能重新声明
# 尝试修改失败
# box_info[0] = 100
# print(f'盒子的长度是{box_info[0]}cm')
# 直接重新定义
box_info = (10,10,10)
for new_value in box_info:
    print(new_value)