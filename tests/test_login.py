# - * - coding = utf-8 - * - #
'''
time: 2025/4/8 16:18
file: test_login.py
author: y79112
'''

import pytest

class TestLogin:
    def test_login(self):
        print('test login')

if __name__ == '__main__':
    pytest.main(['test_login.py'])