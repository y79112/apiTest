# - * - coding = utf-8 - * - #
'''
time: 2025/4/7 19:15
file: get_log.py
author: y79112
'''

from loguru import logger
from time import strftime
from configparser import ConfigParser as cfp
from utils.get_path import configs_path,logs_path
#单例，防止多次生成文件
class Single:
    _danli=False
    def __new__(cls, *args, **kwargs):
        if not cls._danli:
            cls._danli=super().__new__(cls)
        return cls._danli

class Log(Single):
    _flag=True #进入日志文件标志
    def __init__(self):
        self.logConf_file=f'{configs_path}log_conf.ini'

    def get_log(self):
        if self._flag:
            cfg=cfp() #实例化cfp类
            cfg.read(self.logConf_file,encoding='utf-8') #读取配置文件
            _curdate=strftime('%Y-%m-%d')
            logger.remove(handler_id=None) #关闭控制台输出
            logger.add(f'{logs_path}test_{_curdate}.log', #文件名
                       level=cfg.get('log', 'level'),
                       format=cfg.get('log', 'format'),
                       rotation=cfg.get('log', 'rotation'),
                       retention=cfg.get('log', 'retention'),
                       compression=cfg.get('log', 'compression'))

            self._flag=False #关闭标志，防止重复生成文件
        return logger


log=Log().get_log()
if __name__=='__main__':
    log.info('hello world')

