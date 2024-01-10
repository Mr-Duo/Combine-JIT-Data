import argparse, tempfile, shutil
from utils import *
from dict import create_dict

def read_args():
    parser = argparse.ArgumentParser(description='Process JSON data.')
    parser.add_argument('-data_path')
    parser.add_argument('-output_path')
    return parser.parse_args()

def main():
    args = read_args()
    data_path = args.data_path
    output_path = f"{args.output_path}/cross-lang-preprocessed"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for language in os.listdir(data_path):
        language_path = f"{data_path}/{language}"

        for file in os.listdir(language_path):
            file_path = f"{language_path}/{file}"

            commits_path, features_path = os.listdir(file_path)
            commits_path, features_path = f"{file_path}/{commits_path}", f"{file_path}/{features_path}"

            logger(commits_path, features_path)

if __name__ == "__main__":
    main()