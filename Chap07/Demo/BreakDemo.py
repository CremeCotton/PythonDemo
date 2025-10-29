# 使用break结束程序
message = '请输入你想去的城市'
message += '如果输入exit则会退出程序'
while True:
    city = input(message)
    if city == 'exit':
        break
    else:
        print(f'我希望有一天能去{city}旅游!')