# - * - coding = utf-8 - * - #
'''
time: 2025/4/6 14:52
file: login.py
author: y79112
'''

from base.baseApi import BaseApi


class Login(BaseApi):

    def login(self,data):

        res=self.base_send(data=data)
        return res


if __name__ == '__main__':
    login = Login()
    from utils.get_excel import get_excel_data
    data = get_excel_data('登录','Login')

    # res = login.login(data[0][1])
    # res = login.login({'username':'y79112','password':'123'})

    res=login.login(data[4][1])
    print(res.status_code)
    print(res.text)

