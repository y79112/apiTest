# - * - coding = utf-8 - * - #
'''
time: 2025/4/8 16:18
file: test_login.py
author: y79112
'''

import pytest
import allure
from utils.get_excel import get_excel_data

@allure.epic('y79112接口自动化测试项目')
@allure.feature('登录模块')
class TestLogin:
    @allure.story('登录接口')
    @pytest.mark.parametrize('title,inData,expData',get_excel_data('登录','Login'))
    @allure.title('{title}')
    def test_login(self,title,inData,expData,login_init):
        with allure.step('1.获取接口返回数据'):
            res=login_init.login(inData)
        with allure.step('2.断言'):
            assert res.status_code==expData['status_code']


if __name__ == '__main__':
    from utils.get_path import reports_path
    import os
    pytest.main(['-sv','--alluredir',f'{reports_path}tmp','--clean-alluredir'])

    # allure generate allure报告,生成报告-o 后面跟路径，然后--clean 清除之前的报告
    os.system(f'allure generate {reports_path}tmp -o {reports_path}report --clean')
    os.system(f'allure open {reports_path}report -p 8088') #生成报告并启动服务
    # os.system(f'allure serve -h 10.1.1.1 -p 8088 {report_path}report') #生成特定ip+端口的报告网站,仅有-p可访问本机任意ip网站