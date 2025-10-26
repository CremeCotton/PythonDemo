# 使用get来获得值
# 在指定的键不存在时返回一个默认值
# get() 方法的
# 第一个参数用于指定键，是必不可少的
# 第二个参数为当指定的键不存在时要返回的值，是可选的
computer = {
    'brand':'lenovo',
    'build_date':'20250601'
}
# 在字典没有price这个字段的情况下默认是NULL
price_value = computer.get('price','NULL')
print(price_value)