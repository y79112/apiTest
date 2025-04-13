# - * - coding = utf-8 - * - #
'''
time: 2025/4/8 16:10
file: conftest.py
author: y79112
'''

#测试用例执行配置

import pytest
from libs.login import Login

@pytest.fixture(scope='session',autouse=True)
def start_end_test():
    print('\n开始测试...')
    yield
    print('测试结束。')


@pytest.fixture(scope='module')
def login_init(request):
    login_obj = Login()
    yield login_obj