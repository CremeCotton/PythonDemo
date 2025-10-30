# 返回简单值
def get_full_name(first_name,last_name):
    full_name = f'{first_name} {last_name}'
    return full_name
myself = get_full_name('陈','卓伟')
print(myself)

# 让实参变成可选的 按照传参顺序来传参,这里以location为可选参数
def get_company_info(company_name,location,industry):
    info = f'{company_name}是一家{industry}公司,总部是在{location}'
    return info
company = get_company_info('阿里巴巴','杭州','电子商务')
print(company)

def company_info(company_name,location,industry):
    if location:
        info = f'{company_name}是一家{industry}公司,总部是在{location}'
    else:
        info = f'{company_name}是一家{industry}公司'
    return info
tencent = company_info('腾讯','深圳','互联网')
print(tencent)
baidu = company_info('百度',' ','搜索引擎')
print(baidu)