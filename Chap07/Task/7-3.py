# 检查是否是10的整数倍
num = input('请输入一个整数:\n')
if int(num) % 10 == 0:
    print(f'{num}是10的整数倍')
else:
    print(f'{num}不是10的整数倍')