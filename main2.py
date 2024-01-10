import argparse, tempfile, shutil
from utils import *
from dict import create_dict

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
    pathes = [single_path, cross_path]
    output_path = f"{args.output_path}/cross-lang-preprocessed"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for path in pathes:
        for language in os.listdir(path):
            language_path = f"{path}/{language}"

            folders = os.listdir(language_path)
            commits_path, features_path = folders
            commits_path, features_path = f"{language_path}/{commits_path}", f"{language_path}/{features_path}"

            for file in os.listdir(commits_path):
                logger(file)

if __name__ == "__main__":
    main()