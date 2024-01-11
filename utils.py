import os, pickle
import pandas as pd
from datetime import datetime
from icecream import ic as logger
from padding import padding_data
from jit_padding import padding_message, clean_and_reformat_code, padding_commit_code, mapping_dict_msg, mapping_dict_code, convert_msg_to_label

if not os.path.exists(f'{os.getcwd()}/logs'):
    os.makedirs(f'{os.getcwd()}/logs')

# Define a file to log IceCream output
log_file_path = os.path.join(f'{os.getcwd()}/logs', f'{datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.log')

# Replace logging configuration with IceCream configuration
logger.configureOutput(prefix=' - ', outputFunction=lambda x: open(log_file_path, 'a').write(x + '\n'))

LANGAUGE_PROJECTS = {
    'javascript': ['phaser', 'bootstrap', 'moment', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'uppy', 'preact'],
    'java': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'netty', 'jenkins', 'skywalking'],
    'c': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'cpp': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'caffe', 'protobuf', 'tensorflow'],
    'python': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy', 'yolov5'],
}

CROSS_LANGAUGE_PROJECTS = {
    'javascript': ['java', 'c', 'cpp', 'python'],
    'java': ['javascript', 'c', 'cpp', 'python'],
    'c': ['javascript', 'java', 'cpp', 'python'],
    'cpp': ['javascript', 'java', 'c', 'python'],
    'python': ['javascript', 'java', 'c', 'cpp'],
}

def get_list_files_cross(project_name):
    output = [
        f'deepjit_{project_name}_part_4_train.pkl',
        f'deepjit_{project_name}_part_4_val.pkl',
        f'simcom_{project_name}_part_4_train.pkl',
        f'simcom_{project_name}_part_4_val.pkl',
        f'deepjit_{project_name}_part_1_part_4_train.pkl',
        f'deepjit_{project_name}_part_1_part_4_val.pkl',
        f'simcom_{project_name}_part_1_part_4_train.pkl',
        f'simcom_{project_name}_part_1_part_4_val.pkl',
        f'{project_name}_part_4.csv',
        f'{project_name}_part_4_train.csv',
        f'{project_name}_part_4_val.csv'
    ]

    return output

def get_list_files(project_name):
    output = [
        f'deepjit_{project_name}_part_4_train.pkl',
        f'deepjit_{project_name}_part_4_val.pkl',
        f'simcom_{project_name}_part_4_train.pkl',
        f'simcom_{project_name}_part_4_val.pkl',
        f'deepjit_{project_name}_part_1_part_4_train.pkl',
        f'deepjit_{project_name}_part_1_part_4_val.pkl',
        f'simcom_{project_name}_part_1_part_4_train.pkl',
        f'simcom_{project_name}_part_1_part_4_val.pkl',
        f'deepjit_{project_name}_part_5.pkl',
        f'simcom_{project_name}_part_5.pkl',
        f'{project_name}_part_5.csv',
        f'{project_name}_part_4.csv',
        f'{project_name}_part_4_train.csv',
        f'{project_name}_part_4_val.csv'
    ]

    return output

def get_save_name_cross(index, language):
    output = [
        f'{language}/commits/deepjit_{language}_part_4_train.pkl',
        f'{language}/commits/deepjit_{language}_part_4_val.pkl',
        f'{language}/commits/simcom_{language}_part_4_train.pkl',
        f'{language}/commits/simcom_{language}_part_4_val.pkl',
        f'{language}/commits/deepjit_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/deepjit_{language}_part_1_part_4_val.pkl',
        f'{language}/commits/simcom_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/simcom_{language}_part_1_part_4_val.pkl',
        f'{language}/features/{language}_part_4.csv',
        f'{language}/features/{language}_part_4_train.csv',
        f'{language}/features/{language}_part_4_val.csv'
        f'{language}/features/{language}_part_1_part_4.csv',
        f'{language}/features/{language}_part_1_part_4_train.csv',
        f'{language}/features/{language}_part_1_part_4_val.csv'
    ]

    return output[index]

def get_save_name(index, language):
    output = [
        f'{language}/commits/deepjit_{language}_part_4_train.pkl',
        f'{language}/commits/deepjit_{language}_part_4_val.pkl',
        f'{language}/commits/simcom_{language}_part_4_train.pkl',
        f'{language}/commits/simcom_{language}_part_4_val.pkl',
        f'{language}/commits/deepjit_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/deepjit_{language}_part_1_part_4_val.pkl',
        f'{language}/commits/simcom_{language}_part_1_part_4_train.pkl',
        f'{language}/commits/simcom_{language}_part_1_part_4_val.pkl',
        f'{language}/commits/deepjit_{language}_part_5.pkl',
        f'{language}/commits/simcom_{language}_part_5.pkl',
        f'{language}/features/{language}_part_5.csv',
        f'{language}/features/{language}_part_4.csv',
        f'{language}/features/{language}_part_4_train.csv',
        f'{language}/features/{language}_part_4_val.csv'
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
        logger(len(_ids))
        ids += _ids
        msgs += _msgs
        codes += _codes
        labels += _labels

    logger(len(ids))
    return [ids, msgs, codes, labels]

def combine_feature(dir, files):
    data_frame = None

    for file in files:
        logger(f"{dir}/{file}")
    
        if data_frame is None:
            data_frame = pd.read_csv(f"{dir}/{file}")
            logger(data_frame.shape)
        else:
            df = pd.read_csv(f"{dir}/{file}")
            logger(df.shape)
            data_frame = pd.concat([data_frame, df])

    logger(data_frame.shape)
    return data_frame

def preprocess_file(dir, file_name, dict_path, output_path):
    loaded_data = pickle.load(open(f"{dir}/{file_name}", 'rb'))
    ids, messages, codes, labels = loaded_data

    dictionary = pickle.load(open(dict_path, 'rb'))   
    dict_msg, dict_code = dictionary

    pad_msg = padding_data(data=messages, dictionary=dict_msg, type='msg')
    pad_code = padding_data(data=codes, dictionary=dict_code, type='code')

    output = [ids, pad_msg, pad_code, labels]

    save_path = f"{output_path}/{file_name}"
    if not os.path.exists(os.path.dirname(save_path)):
        os.makedirs(os.path.dirname(save_path))
    with open(save_path, 'wb') as file:
        pickle.dump(output, file)