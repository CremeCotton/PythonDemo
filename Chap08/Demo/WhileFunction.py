# 让用户输入姓和名，如果
def get_user_name(first_name,last_name):
    """返回整洁的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    f_name = input("\n请输入你的名字：")
    if f_name.lower() == 'q':
        break
    l_name = input("请输入你的姓氏：")
    if l_name.lower() == 'q':
        break
    user_name = get_user_name(f_name, l_name)
    print(f"\n你好，{user_name}！")