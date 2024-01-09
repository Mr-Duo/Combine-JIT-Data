import os
from datetime import datetime
from icecream import ic as logger

if not os.path.exists(f'{os.getcwd()}/logs'):
    os.makedirs(f'{os.getcwd()}/logs')

# Define a file to log IceCream output
log_file_path = os.path.join(f'{os.getcwd()}/logs', f'{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.log')

# Replace logging configuration with IceCream configuration
logger.configureOutput(prefix=' - ', outputFunction=lambda x: open(log_file_path, 'a').write(x + '\n'))

LANGAUGE_PROJECTS = {
    'javascript': ['phaser', 'bootstrap', 'moment', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'uppy', 'preact', 'iptv'],
    'java': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'netty', 'jenkins', 'skywalking', 'Java'],
    'c': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'cpp': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'caffe', 'protobuf', 'rocksdb', 'tensorflow'],
    'python': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy', 'yolov5'],
}

FILE_INDEX = {
    '_part_1_part_4_train_dict.pkl',
    'cc2vec_{}_part_1_part_4_train.pkl'
}

'bootstrap_part_1_part_4_train_dict.pkl',
'cc2vec_bootstrap_part_1_part_4_train.pkl',
'cc2vec_bootstrap_part_1_part_4_val.pkl',
'deepjit_bootstrap_part_1_part_4_train.pkl',
'deepjit_bootstrap_part_1_part_4_val.pkl',
'simcom_bootstrap_part_1_part_4_train.pkl',
'simcom_bootstrap_part_1_part_4_val.pkl',
'cc2vec_bootstrap_part_5.pkl',
'deepjit_bootstrap_part_5.pkl',
'simcom_bootstrap_part_5.pkl',
'bootstrap_part_5.csv',
'bootstrap_part_1_part_4.csv',
'bootstrap_part_1_part_4_train.csv',
'bootstrap_part_1_part_4_val.csv',

def get_list_files(project_name):
    output = [
        f'{project_name}_part_1_part_4_train_dict.pkl',
        f'cc2vec_{project_name}_part_1_part_4_train.pkl',
        f'cc2vec_{project_name}_part_1_part_4_val.pkl',
        f'deepjit_{project_name}_part_1_part_4_train.pkl',
        f'deepjit_{project_name}_part_1_part_4_val.pkl',
        f'simcom_{project_name}_part_1_part_4_train.pkl',
        f'simcom_{project_name}_part_1_part_4_val.pkl',
        f'cc2vec_{project_name}_part_5.pkl',
        f'deepjit_{project_name}_part_5.pkl',
        f'simcom_{project_name}_part_5.pkl',
        f'{project_name}_part_5.csv',
        f'{project_name}_part_1_part_4.csv',
        f'{project_name}_part_1_part_4_train.csv',
        f'{project_name}_part_1_part_4_val.csv'
    ]

    return output