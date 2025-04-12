# - * - coding = utf-8 - * - #
'''
time: 2025/4/7 19:49
file: get_path.py
author: y79112
'''


import os

pro_path=os.path.dirname(os.path.dirname(__file__))

configs_path=os.path.join(pro_path,'configs\\')
out_path=os.path.join(pro_path,'out\\')
logs_path=os.path.join(out_path,'logs\\')
testCases_path=os.path.join(pro_path,'testCases\\')


if __name__ == '__main__':
    print(logs_path)