name = '请输入您的姓名,如果输入eixt则会自动退出程序\n'
message = input(name)
while message != 'exit':
    print(f'您好,{message}!')
    message = input(name)