#!/usr/bin/env python3

import os
import requests
from changeImage import get_list_of_files_from_directory

def upload_file_to_the_server(file_path, server_url):
    """
    Uploads file from file_path to a server specified by server_url
    """
    with open(file_path, 'rb') as opened_file:
        r = requests.post(server_url, files={"file": opened_file})

def get_full_path_list_of_files(source_directory, file_extension):
    """
    Returns the list of full paths to the files with specified file_extension
    from the source_directory
    """
    full_path_list = []
    file_list = get_list_of_files_from_directory(source_directory,
                                                 file_extension)
    for file_name in file_list:
        full_path = os.path.join(source_directory, file_name)
        if os.path.isfile(full_path):
            full_path_list.append(full_path)
    return full_path_list

def upload_all_from_the_list_to_url(full_path_list, server_url):
    """
    Uploads all existing files from the list to the server url
    """
    for file_full_path in full_path_list:
        if os.path.isfile(file_full_path):
            try:
                upload_file_to_the_server(file_full_path, server_url)
            except:
                print(
                    "Upload error: {} wasn't loaded to the server {}".
                        format(file_full_path, server_url)
                    )

def upload_all_from_the_source_directory(source_directory,
                                         file_extension, server_url):
    """
    Uploads all files with specified file_extension from a specified
    source_directory to a server
    """
    full_path_list = get_full_path_list_of_files(source_directory,
                                                 file_extension)
    upload_all_from_the_list_to_url(full_path_list, server_url)

def main():
    server_url = "http://localhost/upload/"
    source_directory = "./supplier-data/images"
    file_extension = "*.jpeg"
    upload_all_from_the_source_directory(source_directory,
                                         file_extension, server_url)


if __name__ == '__main__':
    main()
