import os, pickle
import pandas as pd
from datetime import datetime
from icecream import ic as logger
from padding import padding_data

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

SINGLE_PROJECTS = {
    'phaser': ['bootstrap', 'moment', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'uppy', 'preact'],
    'bootstrap': ['phaser', 'moment', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'uppy', 'preact'],
    'moment': ['phaser', 'bootstrap', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'uppy', 'preact'],
    'Ghost': ['phaser', 'bootstrap', 'moment', 'mongoose', 'eslint', 'codemirror5', 'uppy', 'preact'],
    'mongoose': ['phaser', 'bootstrap', 'moment', 'Ghost', 'eslint', 'codemirror5', 'uppy', 'preact'],
    'eslint': ['phaser', 'bootstrap', 'moment', 'Ghost', 'mongoose', 'codemirror5', 'uppy', 'preact'],
    'codemirror5': ['phaser', 'bootstrap', 'moment', 'Ghost', 'mongoose', 'eslint', 'uppy', 'preact'],
    'uppy': ['phaser', 'bootstrap', 'moment', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'preact'],
    'preact': ['phaser', 'bootstrap', 'moment', 'Ghost', 'mongoose', 'eslint', 'codemirror5', 'uppy'],
    'elasticsearch': ['flink', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'netty', 'jenkins', 'skywalking'],
    'flink': ['elasticsearch', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'netty', 'jenkins', 'skywalking'],
    'shardingsphere': ['elasticsearch', 'flink', 'presto', 'keycloak', 'kafka', 'netty', 'jenkins', 'skywalking'],
    'presto': ['elasticsearch', 'flink', 'shardingsphere', 'keycloak', 'kafka', 'netty', 'jenkins', 'skywalking'],
    'keycloak': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'kafka', 'netty', 'jenkins', 'skywalking'],
    'kafka': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'keycloak', 'netty', 'jenkins', 'skywalking'],
    'netty': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'jenkins', 'skywalking'],
    'jenkins': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'netty', 'skywalking'],
    'skywalking': ['elasticsearch', 'flink', 'shardingsphere', 'presto', 'keycloak', 'kafka', 'netty', 'jenkins'],
    'php-src': ['TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'TDengine': ['php-src', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'mpv': ['php-src', 'TDengine', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'openssl': ['php-src', 'TDengine', 'mpv', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'lede': ['php-src', 'TDengine', 'mpv', 'openssl', 'netdata', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'netdata': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'emscripten', 'redis', 'obs-studio', 'libuv'],
    'emscripten': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'redis', 'obs-studio', 'libuv'],
    'redis': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'obs-studio', 'libuv'],
    'obs-studio': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'libuv'],
    'libuv': ['php-src', 'TDengine', 'mpv', 'openssl', 'lede', 'netdata', 'emscripten', 'redis', 'obs-studio'],
    'yuzu': ['swift', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'caffe', 'protobuf', 'tensorflow'],
    'swift': ['yuzu', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'caffe', 'protobuf', 'tensorflow'],
    'tesseract': ['yuzu', 'swift', 'carbon-lang', 'grpc', 'electron', 'caffe', 'protobuf', 'tensorflow'],
    'carbon-lang': ['yuzu', 'swift', 'tesseract', 'grpc', 'electron', 'caffe', 'protobuf', 'tensorflow'],
    'grpc': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'electron', 'caffe', 'protobuf', 'tensorflow'],
    'electron': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'grpc', 'caffe', 'protobuf', 'tensorflow'],
    'caffe': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'protobuf', 'tensorflow'],
    'protobuf': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'caffe', 'tensorflow'],
    'tensorflow': ['yuzu', 'swift', 'tesseract', 'carbon-lang', 'grpc', 'electron', 'caffe', 'protobuf'],
    'cpython': ['salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy',  'yolov5'],
    'salt': ['cpython', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy',  'yolov5'],
    'pandas': ['cpython', 'salt', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy',  'yolov5'],
    'transformers': ['cpython', 'salt', 'pandas', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy',  'yolov5'],
    'scipy': ['cpython', 'salt', 'pandas', 'transformers', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy',  'yolov5'],
    'scikit-learn': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'numpy', 'jumpserver', 'scrapy',  'yolov5'],
    'numpy': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'jumpserver', 'scrapy',  'yolov5'],
    'jumpserver': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'scrapy',  'yolov5'],
    'scrapy': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver',  'yolov5'],
    'yolov5': ['cpython', 'salt', 'pandas', 'transformers', 'scipy', 'scikit-learn', 'numpy', 'jumpserver', 'scrapy'],
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
        f'{project_name}_part_4_val.csv',
        f'{project_name}_part_1_part_4.csv',
        f'{project_name}_part_1_part_4_train.csv',
        f'{project_name}_part_1_part_4_val.csv'
    ]

    return output

def get_list_files(project_name):
    output = [
        f'change_codes_deepjit_{project_name}_train.pkl',
        f'change_codes_deepjit_{project_name}_val.pkl',
        f'change_codes_deepjit_{project_name}_test.pkl',
        f'change_codes_simcom_{project_name}_train.pkl',
        f'change_codes_simcom_{project_name}_val.pkl',
        f'change_codes_simcom_{project_name}_test.pkl',
        f'change_features_{project_name}_train.csv',
        f'change_features_{project_name}_val.csv',
        f'change_features_{project_name}_test.csv',
    ]

    return output

def get_save_name_cross(index, language):
    output = [
        f'{language}/commits/change_codes_deepjit_{language}_train.pkl',
        f'{language}/commits/change_codes_deepjit_{language}_val.pkl',
        f'{language}/commits/change_codes_deepjit_{language}_test.pkl',
        f'{language}/commits/change_codes_simcom_{language}_train.pkl',
        f'{language}/commits/change_codes_simcom_{language}_val.pkl',
        f'{language}/commits/change_codes_simcom_{language}_test.pkl',
        f'{language}/features/change_features_{language}_train.csv',
        f'{language}/features/change_features_{language}_val.csv',
        f'{language}/features/change_features_{language}_test.csv',
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
        f'{language}/features/{language}_part_4_val.csv',
        f'{language}/features/{language}_part_1_part_4.csv',
        f'{language}/features/{language}_part_1_part_4_train.csv',
        f'{language}/features/{language}_part_1_part_4_val.csv'
    ]

    return output[index]

def combine_commit(dir, files):
    logger(files)
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
    logger(files)
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