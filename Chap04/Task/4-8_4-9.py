# 1-10的立方 要求使用for循环
base_list = range(1,11)
for value in base_list:
    print(value**3)

# 同样的，要求使用列表解析
value = [value**3 for value in range(1,11)]
print(value)