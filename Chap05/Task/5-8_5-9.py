# 结合使用for循环和if来检查
current_list = ['admin','Jason','Clay','Stella','Ray']
for user in current_list:
    if user == 'admin':
        print('管理员登录!')
    else:
        print(f'{user}用户欢迎登录')

# 如果没有用户则输出对应内容
if len(current_list) == 0:
    print('用户名单是空的')
else:
    print('用户名单不是空的') 