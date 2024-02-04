#!/usr/bin/bash

###################################################################
#Script Name	: metadata_to_csv in Docker
#Description	: will build and run metadata_to_csv script in Docker
#                 and output CSV dataset in this project's directory
#Args           : no inputed args
#                 but populate @absolutePathToFiles with the absolute path to
#                 this project root
#Author       	: socraticDevBlog
#Email         	:
###################################################################

##
#    TWO FIRST VARIABLES MUST BE CHANGED BY USER BEFORE RUNNING SCRIPT
#      - csvFileName
#      - absolutePathToFiles
##

##
# VALUE MUST MATCH CONFIGS: look for key "csv_file_name" in config.yml file
csvFileName="example_metadata.csv"
##

##
# replace this value by the absolute file path to this project on your local filesystem
absolutePathToFiles= </the/absolute/path/metadata_to_csv >/${dirName}
##

imageName="metadata_to_csv"
containerName="metadata_to_csv_container"
dirName="example_files"

docker build -t ${imageName} .

docker run -v ${absolutePathToFiles}:/app/${dirName} --name ${containerName} ${imageName} ${dirName}

docker cp ${containerName}:/app/${csvFileName} .

docker rm ${containerName}
