# 使用标志
acitve = True
while acitve:
    message = input('请输入您的姓名,如果输入eixt则会自动退出程序\n')
    if message == 'exit':
        acitve = False
    else:
        print(f'您好,{message}!')