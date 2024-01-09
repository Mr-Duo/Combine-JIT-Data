import os, pickle
import pandas as pd
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

def get_list_files(project_name):
    output = [
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

def get_save_name(index, language):
    output = [
        f'{language}/commits/cc2vec_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/cc2vec_{language}_part_1_part_4_val.pkl',
        f'{language}/commits/deepjit_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/deepjit_{language}_part_1_part_4_val.pkl',
        f'{language}/commits/simcom_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/simcom_{language}_part_1_part_4_val.pkl',
        f'{language}/commits/cc2vec_{language}_part_5.pkl',
        f'{language}/commits/deepjit_{language}_part_5.pkl',
        f'{language}/commits/simcom_{language}_part_5.pkl',
        f'{language}/features/{language}_part_5.csv',
        f'{language}/features/{language}_part_1_part_4.csv',
        f'{language}/features/{language}_part_1_part_4_train.csv',
        f'{language}/features/{language}_part_1_part_4_val.csv'
    ]

    return output[index]

def combine_commit(dir, files):
    ids, msgs, codes, labels = [], [], [], []

    for file in files:
        logger(f"{dir}/{file}")
        loaded_data = pickle.load(open(f"{dir}/{file}", 'rb'))
        _ids, _msgs, _codes, _labels = loaded_data
        logger(len(_ids), len(_msgs), len(_codes), len(_labels))
        ids += _ids
        msgs += _msgs
        codes += _codes
        labels += _labels

    logger(len(ids), len(msgs), len(codes), len(labels))
    return [ids, msgs, codes, labels]

def combine_feature(dir, files):
    data_frame = pd.DataFrame()

    for file in files:
        logger(f"{dir}/{file}")
        df = pd.read_csv(f"{dir}/{file}")
        logger(df.shape)
        data_frame = pd.concat([data_frame, df])

    logger(data_frame.shape)
    return data_frame