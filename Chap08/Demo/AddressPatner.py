# 位置实参
def my_info(name,age,level):
    print(f'我的姓名是{name}，年龄是{age}，就读于{level}')
my_info('张三',18,'高中')

# 多次调用
def pet_info(type,name,age):
    print(f'我有一只{type}，它的名字叫{name}')
    print(f'我的{type}今年{age}岁了')
pet_info('狗','大黄',3)

# 位置实参需要注意顺序
def car_info(brand,model,year):
    print(f'我有一辆{year}年的{brand}牌{model}汽车')
car_info('宝马','X5',2020)
car_info('X5','宝马',2020)  # 错误示范

# 关键字实参 顺序可以打乱
def university_info(en_name,location,cn_name):
    print(f'{cn_name}的英文名称是{en_name}，位于{location}')
# 顺序完全打乱
university_info(en_name='Tsinghua University',location='Beijing',cn_name='清华大学')
# 按照顺序
university_info(cn_name='北京大学',en_name='Peking University',location='Beijing')

# 默认值 默认值要放在最后面
def computer_info(model,price,brand='Lenovo'):
    print(f'我有一台{brand}牌的{model}电脑,价格是{price}元')
computer_info('Thinkpad X1 Carbon',12000)

# 混合调用
def house_info(size,city):
    print(f'我在{city}有一套{size}平米的房子')
house_info(120,'上海')  # 位置实参
house_info(size=150,city='北京')  # 关键字实参
house_info(200,city='广州')  # 混合调用