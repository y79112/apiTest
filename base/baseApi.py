# - * - coding = utf-8 - * - #
'''
time: 2025/4/6 14:50
file: baseApi.py
author: y79112
'''

from utils.get_log import log
from requests import request
import inspect
from utils.get_yml_data import get_yml_data
from utils.get_path import configs_path


class BaseApi:
    def __init__(self):
        api_conf_file=f'{configs_path}api_config.yml'
        yml_data=get_yml_data(api_conf_file)
        self.api_data=yml_data[self.__class__.__name__]
        self.HOST=yml_data['HOST']

    def base_send(self,**kwargs): #基础发送方法
        try:
            method_name=inspect.stack()[1][3] #调用此方法的方法名
            method=self.api_data[method_name]['method']
            api_path=self.api_data[method_name]['path']
            res=request(method=method,
                url=f'{self.HOST}{api_path}',
                **kwargs
                )
            log.info(f'''
            请求地址: {res.request.url}
            请求方法: {res.request.method}
            请求模块: {self.__class__.__name__}
            请求内容: {res.request.body}
            响应内容: {res.text}
            响应状态: {res.status_code}
            ''')
            return res
        except Exception as e:
            log.error(e)

    #增加
    def add(self,**kwargs):
        return self.base_send(**kwargs)
    #删除
    def delete(self,**kwargs):
        return self.base_send(**kwargs)

    #更新
    def update(self,**kwargs):
        return self.base_send(**kwargs)

    #查询
    def query(self,**kwargs):
        return self.base_send(**kwargs)