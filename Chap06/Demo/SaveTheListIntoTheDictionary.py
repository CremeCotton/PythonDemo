# 在字典中存储列表
apple = {
    'country':'美国',
    'products':['iphone','ipad','mac','appele watch']
}
print(f'此品牌来自{apple['country']}')
for product in apple['products']:
    print(product)