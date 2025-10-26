# 已经使用的名称列表
current_users = ['Clay','Jason','Ray','Stella','Sonny']
wait_users = ['Clay','Ray','Stella']

# 开始检查，有或者没有都输出相关信息
for user in current_users:
    if user in wait_users:
        print(f'{user}已被使用')
    if user not in wait_users:
        print(f'{user}未被使用')