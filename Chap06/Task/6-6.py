# 检查用户名使用情况
checked_users = ['Jason','Clay','Ray']
wait_users = ['Jason','Clay','Stella']

for user in wait_users:
    if user in checked_users:
        print(f'{user}已检查')
    else:
        print(f'{user}还没检查')