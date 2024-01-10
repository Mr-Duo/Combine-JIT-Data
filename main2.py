import argparse
from utils import *

def read_args():
    parser = argparse.ArgumentParser(description='Process JSON data.')
    parser.add_argument('-single_path')
    parser.add_argument('-cross_path')
    parser.add_argument('-output_path')
    return parser.parse_args()

def main():
    args = read_args()
    single_path = args.single_path
    cross_path = args.cross_path
    output_path = f"{args.output_path}/cross-lang-preprocessed"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for language in os.listdir(cross_path):
        language_path = f"{cross_path}/{language}"

        folders = os.listdir(language_path)
        commits_path, features_path = folders[0], folders[1]
        commits_path, features_path = f"{language_path}/{commits_path}", f"{language_path}/{features_path}"

        for file in os.listdir(commits_path):
            if 'dict' in file:
                logger(file)

    for language in os.listdir(single_path):
        language_path = f"{single_path}/{language}"

        folders = os.listdir(language_path)
        commits_path, features_path = folders[0], folders[1]
        commits_path, features_path = f"{language_path}/{commits_path}", f"{language_path}/{features_path}"

        for file in os.listdir(commits_path):
            if 'part_5' in file:
                logger(file)

    for language in os.listdir(cross_path):
        language_path = f"{cross_path}/{language}"

        folders = os.listdir(language_path)
        commits_path, features_path = folders[0], folders[1]
        commits_path, features_path = f"{language_path}/{commits_path}", f"{language_path}/{features_path}"

        for file in os.listdir(commits_path):
            if 'dict' not in file:
                logger(file)

if __name__ == "__main__":
    main()