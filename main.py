import os, sys, logging
from typing import List
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


def get_all_files_from(directory: str) -> List[str]:
    """

    Walks given directory tree and returns all files path in a list

    Parameters:
    - directory (str): name of the directory to extract files from

    Returns:
    List[str]: a list of the path to all files contained within given directory

    """
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            full_path = os.path.join(root, filename)
            files.append(os.path.abspath(full_path))
    return files


def get_all_metadata_from(files: List[str], encoding: str) -> List:
    """

    Discovers keys from frontmatter and extracts all of its metadata

    Parameters:
    - files: List of strings that are absolute paths toward files

    Returns:
    - List of metadata objects (dictionaries)

    """
    metadata_list = []
    for file in files:
        with open(file, encoding=encoding) as f:
            metadata_obj = {}
            content = frontmatter.load(f)
            for key in sorted(content.keys()):
                metadata_obj[key] = content[key]

            metadata_obj["filepath"] = file

            metadata_list.append(metadata_obj)

    return metadata_list


def main(dir_path: str, encoding: str, csv_filename: str) -> None:
    files = get_all_files_from(dir_path)
    metadata_list = get_all_metadata_from(files=files, encoding=encoding)

    df = pd.DataFrame(metadata_list)
    df.to_csv(csv_filename, index=False)


if __name__ == "__main__":
    print(PRODUCT_ASCII)
    print(LICENSE_TXT)

    try:
        files_directory_name = sys.argv[1]
    except:
        print("No root directory argument was given as first parameter")
        print("root file directory(within current directory) name is expected\r")
        sys.exit(1)

    try:
        with open("config.yml", "r") as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)
            logging.basicConfig(
                level=(
                    logging.INFO if config["logging_level"] == "INFO" else logging.ERROR
                ),
                format="%(asctime)s [%(levelname)s] %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
    except Exception as e:
        logging.error("could not read configuration file config.yml and set logger")
        sys.exit(1)

    try:
        csv_filename = sys.argv[2]
    except:
        csv_filename = config["csv_file_name"]
        logging.info(
            "no csv_filename provided as second argument. will use configured value"
        )

    try:
        main(
            f"{os.getcwd()}{os.sep}{files_directory_name}",
            encoding=config["encoding"],
            csv_filename=csv_filename,
        )
    except Exception as e:
        logging.error(f"could not produce CSV file")
        logging.error(f"details: {str(e)}", exc_info=True)
        sys.exit(1)

    logging.info(
        f'find your CSV metadata file at: {os.getcwd()}{os.sep}{config["csv_file_name"]}'
    )
    sys.exit(0)
