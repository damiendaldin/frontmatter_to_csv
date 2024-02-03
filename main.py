import os, sys
import frontmatter
import pandas as pd
import yaml


def main(dir_path: str, config: dict) -> int:
    directory = os.fsencode(dir_path)

    files = []
    for file_path in os.listdir(directory):
        full_path = os.path.join(dir_path, file_path.decode(config["encoding"]))
        if os.path.isfile(full_path):
            files.append(full_path)

    metadata_list = []
    for file in files:
        with open(file) as f:
            metadata_obj = {}
            content = frontmatter.load(f)
            for key in config["fields"]:
                metadata_obj[key] = content[key]

            metadata_list.append(metadata_obj)

    df = pd.DataFrame(metadata_list)
    df.to_csv(config["csv_file_name"], index=False)

    return 0


if __name__ == "__main__":
    try:
        files_directory_name = sys.argv[1]
    except:
        print("No arguments were given")
        print("file directory name is expected\r")
        exit(1)

    with open("config.yml", "r") as config_file:
        config = yaml.load(config_file, Loader=yaml.FullLoader)
        print("read config file successfully\r")
    return_code = main(f"{os.getcwd()}/{files_directory_name}/", config=config)
    if return_code == 0:
        print(f'find your CSV metada file at: {os.getcwd()}/{config["csv_file_name"]}')
    else:
        print("an error occured, so sorry")
    
    exit(return_code)
