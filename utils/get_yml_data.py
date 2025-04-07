# - * - coding = utf-8 - * - #
'''
time: 2025/4/7 20:29
file: get_yml_data.py
author: y79112
'''


import yaml
from utils.get_path import configs_path
def get_yml_data(yml_file):
    # yml_file = os.path.join(configs_path, 'api_config.yml')
    with open(yml_file, 'r') as f:
        yml_data = yaml.safe_load(f.read())
    return yml_data

if __name__ == '__main__':
    yml_file=f'{configs_path}api_config.yml'
    yml_data = get_yml_data(yml_file)
    print(yml_data)