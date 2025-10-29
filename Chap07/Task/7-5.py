# 对不同年龄的人员收取不同的费用
message = '请输入您的年龄\n'
while True:
    age = input(message)
    if age == 'quit':
        break
    elif int(age) <3:
        print('您是免费入场')
    elif 3 <= int(age) <= 12:
        print('您的入场费用是10美元')
    elif int(age) > 12:
        print('您的入场费用是15美元')