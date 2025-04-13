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


@pytest.fixture(scope='session')
def login_init():
    login_obj = Login()
    yield login_obj


def pytest_collection_modifyitems(config, items):
    """修改收集到的测试项"""
    for item in items:
        # 处理节点ID中的Unicode字符
        if isinstance(item.nodeid, str):
            item._nodeid = item.nodeid.encode('utf-8').decode('unicode_escape')

