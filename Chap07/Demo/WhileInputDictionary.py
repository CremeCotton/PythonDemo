# 使用用户输入来填充字典
students = {}

while True:
    # 输入学生姓名
    name = input("请输入学生姓名: ")
    # 输入学生分数
    score = input("请输入成绩: ")
    # 将学生的姓名和分数进行绑定
    students[name] = score
    
    if input("继续输入？(y/n): ").lower() != 'y':
        break

print("\n学生成绩单:")
for name, score in students.items():
    print(f"{name}: {score}")