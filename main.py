import os, sys
import frontmatter
import pandas as pd
import yaml

LICENSE_TXT = """
    metadata_to_csv  Copyright (C) 2024  Maxime Bonin
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

"""

PRODUCT_ASCII = """
                _            _       _           _                         
 _ __ ___   ___| |_ __ _  __| | __ _| |_ __ _   | |_ ___     ___ _____   __
| '_ ` _ \ / _ \ __/ _` |/ _` |/ _` | __/ _` |  | __/ _ \   / __/ __\ \ / /
| | | | | |  __/ || (_| | (_| | (_| | || (_| |  | || (_) | | (__\__ \\ V / 
|_| |_| |_|\___|\__\__,_|\__,_|\__,_|\__\__,_|___\__\___/___\___|___/ \_/  
                                            |_____|    |_____|  
"""


def main(dir_path: str, config: dict) -> None:
    directory = os.fsencode(dir_path)

    files = []
    for file_path in os.listdir(directory):
        full_path = os.path.join(dir_path, file_path.decode(config["encoding"]))
        absolute_path = os.path.abspath(full_path)
        if os.path.isfile(absolute_path):
            files.append(absolute_path)

    metadata_list = []
    for file in files:
        with open(file, encoding=config["encoding"]) as f:
            metadata_obj = {}
            content = frontmatter.load(f)
            for key in config["fields"]:
                metadata_obj[key] = content[key]

            metadata_list.append(metadata_obj)

    df = pd.DataFrame(metadata_list)
    df.to_csv(config["csv_file_name"], index=False)


if __name__ == "__main__":
    print(PRODUCT_ASCII)
    print(LICENSE_TXT)

    try:
        files_directory_name = sys.argv[1]
    except:
        print("No arguments were given")
        print("file directory(within current directory) name is expected\r")
        exit(1)

    try:
        with open("config.yml", "r") as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
            print("read config file successfully\r")
        main(f"{os.getcwd()}{os.sep}{files_directory_name}", config=config)
        print(
            f'find your CSV metada file at: {os.getcwd()}{os.sep}{config["csv_file_name"]}'
        )
    except:
        print("an error occured, so sorry")

    exit(0)
