def translate_info(cn_name,en_name):
    college = {
        'cn_name':cn_name,
        'en_name':en_name
    }
    return college
my_college = translate_info('清华大学','Tsinghua University')
print(my_college)
