# - * - coding = utf-8 - * - #
'''
time: 2025/4/13 16:14
file: encrypted_data.py
author: y79112
'''

import hashlib

def get_md5(data,salt=''):

    m = hashlib.md5()
    data=(data+salt).encode('utf-8')
    m.update(data)
    return m.hexdigest()

if __name__ == '__main__':
    pwd='123'
    salt='测试'
    print(get_md5(pwd,salt))