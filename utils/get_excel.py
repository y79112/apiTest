# - * - coding = utf-8 - * - #
'''
time: 2025/4/12 10:53
file: get_excel.py
author: y79112
'''

import xlrd
from utils.get_path import testCases_path,configs_path
from utils.get_yml_data import get_yml_data

def get_excel_data(sheet_name,module_name):
    '''
    读取excel 用例数据
    :param sheet_name: excel工作簿名称
    :param module_name: 模块名称
    :return: 筛选后的用例数据 [[用例1],[用例2],[用例3]]
    '''

    #最终返回列表
    result_list=[]
    #筛选行列表
    row_list=[]
    #筛选列列表
    col_list=[]

    #筛选数据
    testCaseConf_file=f'{configs_path}testCaseConf.yml'
    sel_data=get_yml_data(testCaseConf_file)
    #筛选行
    row_sel=sel_data[module_name]['rows']
    #筛选列
    col_sel=sel_data[module_name]['cols']

    #打开excel文件
    excel_file=f'{testCases_path}{sel_data['testCaseFile']}'
    file_obj=xlrd.open_workbook(excel_file,formatting_info=True)
    #打开工作表
    sheet_list=file_obj.sheet_by_name(sheet_name)

    #获取第一行所有列
    cols=sheet_list.row_values(0)
    # 获取第一列所有行
    rows=sheet_list.col_values(0)


   #实现选择用例功能
   #选择取哪几行用例
    if 'all' in row_sel:
        row_list=rows[1:]
    else:
        for row in row_sel:
            if '-' in row:
                start,end=row.split('-') #['1-3']
                for j in range(int(start),int(end)+1):
                    row_list.append(f'{module_name.lower()}{j:03}')
            else:
                row_list.append(f'{module_name.lower()}{int(row):03}')

   #选择取哪几列值
    for col in col_sel:
        col_list.append(cols.index(col))

    for row in row_list:
        result_p=[] #中间列表
        for col in col_list:
            result_p.append(sheet_list.cell(rows.index(row), col).value)

        result_list.append(result_p)

    return result_list

if __name__ == '__main__':
    testCaseConf_file=f'{configs_path}testCaseConf.yml'
    module_name='Login'
    caseConf_data=get_yml_data(testCaseConf_file)
    case_file=f'{testCases_path}{caseConf_data['testCaseFile']}'
    sheet_name=caseConf_data[module_name]['sheet_name']
    data=get_excel_data(sheet_name,module_name='Login')
    from pprint import pprint
    pprint(data)
