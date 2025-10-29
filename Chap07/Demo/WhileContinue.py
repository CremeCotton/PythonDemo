# 输出1-100的之间的奇数
begin = 1
while begin <= 100:
    if begin % 2 == 0:
        begin += 1
        continue
    print(begin)
    begin += 1