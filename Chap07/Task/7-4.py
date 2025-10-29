message = '请输入您想添加的食材'
message += "\n(输入'quit'退出程序): "
active = True
while active:
    food = input(message)
    if food != 'quit':
        print(f'我们会将{food}添加到您的披萨中')
    else:
        active = False