# 在字典中存储字典
users = {
    'xiaomi':{
        'first_name':'小',
        'last_name':'米',
        'location':'北京'
    },
    'zhangsan':{
        'first_name':'张',
        'last_name':'三',
        'location':'杭州'
    }
}
for username, user_info in users.items():
    print(f'用户英文名称是{username}')
    full_name = user_info['first_name'] + ' ' +user_info['last_name']
    location = user_info['location']

    print(f'全名是{full_name}')
    print(f'地址是{location}')