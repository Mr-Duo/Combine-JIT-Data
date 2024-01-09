import argparse, tempfile, shutil
from utils import *

def read_args():
    parser = argparse.ArgumentParser(description='Process JSON data.')
    parser.add_argument('-data_path')
    parser.add_argument('-output_path')
    return parser.parse_args()

def main():
    args = read_args()
    data_path = args.data_path
    output_path = f"{args.output_path}/cross-lang-tandataset"

    if not os.path.exists(output_path):
        os.mkdir(output_path)

    for language, projects in LANGAUGE_PROJECTS.items():
        logger(f"{language}: {len(projects)} projects")

        tmp_out_dir = tempfile.mkdtemp(prefix='language.', dir=output_path)
        sub_dirs = []
        for i in range(20):
            tmp_sub_dir = tempfile.mkdtemp(prefix=f'sub_{i}.', dir=tmp_out_dir)
            sub_dirs.append(tmp_sub_dir)

        for project in projects:

            path = f"{data_path}/{project}"
            commits_path, features_path = os.listdir(path)
            commits_path, features_path = f"{path}/{commits_path}", f"{path}/{features_path}"
            
            commit_files = os.listdir(commits_path)
            feature_files = os.listdir(features_path)

            index = 0
            for file in feature_files:
                if 'part_1' in file or 'part_5' in file:
                    file_path = f"{features_path}/{file}"
                    shutil.copy(file_path, sub_dirs[index])
                    index += 1

            for file in commit_files:
                if 'part_1' in file or 'part_5' in file:
                    file_path = f"{commits_path}/{file}"
                    shutil.copy(file_path, sub_dirs[index])
                    index += 1
                
        # shutil.rmtree(tmp_out_dir)
        
        break

if __name__ == "__main__":
    main()