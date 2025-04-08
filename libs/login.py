# - * - coding = utf-8 - * - #
'''
time: 2025/4/6 14:52
file: login.py
author: y79112
'''

from base.baseApi import BaseApi


class Login(BaseApi):

    def login(self, username, password):
        data = {
            'username': username,
            'password': password
        }

        res=self.base_send(data=data)
        return res


if __name__ == '__main__':
    login = Login()
    res = login.login('y79112', '123')
    print(res)

