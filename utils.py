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
