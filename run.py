#!/usr/bin/env python3

import os
import requests
import json
from changeImage import get_list_of_files_from_directory
from supplier_image_upload import get_full_path_list_of_files

def convert_str_weight_into_int(weight):
    """
    Converts part of str before the first space into int value
    """
    try:
        return int(weight.split(" ", 1)[0])
    except ValueError as e:
        print ("Error: {} \nThe default value {} was asigned".format(e, "0"))
        return 0

def convert_txt_description_into_lines(product_description_full_path):
    """
    Creates a list of lines from a product description file the using full path
    """
    try:
        with open(product_description_full_path, "r") as product_description_file:
            product_description_lines = product_description_file.readlines()
        # Remove whitespace characters at the end of each line
        product_description_lines = [
                                  line.strip() for line in product_description_lines
                                  ]
    except ValueError as e:
        print("Error {} \nDefault empty string values were assigned".format(e))
        product_description_lines = ["","","",""]
    return product_description_lines

def get_file_name_from_full_path(full_path_to_file):
    """
    Returns file name without extension from the full path
    """
    try:
        return os.path.splitext(os.path.basename(full_path_to_file))[0]
    except ValueError as e:
        print("Error: {} \nDefault empty string value was returned".format(e))
        return ""

def get_file_name_from_full_path_with_extension(full_path_to_file):
    """
    Returns file name without extension from the full path
    """
    try:
        return os.path.basename(full_path_to_file)
    except ValueError as e:
        print("Error: {} \nDefault empty string value was returned".format(e))
        return ""

def create_product_json(product_description_full_path, product_img_full_path):
    """
    Created json table with product description and an image file name
    """
    product_description_dict = {}
    image_name = get_file_name_from_full_path_with_extension(product_img_full_path)
    product_description_lines = convert_txt_description_into_lines(
                              product_description_full_path)
    # Convert str weight value into int weight value
    product_description_lines[1] = convert_str_weight_into_int(
                                 product_description_lines[1])
    # Populate product_description_dict with Name, Weight, Descriptiom, img name
    product_description_dict = {
                             "name": product_description_lines[0],
                             "weight": product_description_lines[1],
                             "description": product_description_lines[2],
                             "image_name": image_name
                             }
    return product_description_dict

def upload_description_to_the_server(full_description, server_url):
    """
    Uploads json dictionary with description to the server
    """
    try:
        response = requests.post(server_url, json=full_description)
    except ValueError as e:
        print("Error {}".format(e))

def match_img_to_description(
        product_description_full_path,
        product_img_full_path):
    """
    Checks if description matches corresponding images using file name
    """
    d_name = get_file_name_from_full_path(product_description_full_path)
    i_name = get_file_name_from_full_path(product_img_full_path)
    return d_name == i_name

def upload_all_descriptions_from_a_folder(
        sourse_description_directory,
        sourse_description_extension,
        sourse_img_directory,
        source_img_extension,
        server_url):
    """
    Goes through all descriptions in a folder
    matches descriptions with corresponding images using file name
    uploads descriptions to the server
    """
    description_path_list = get_full_path_list_of_files(
                          sourse_description_directory,
                          sourse_description_extension)
    img_path_list = get_full_path_list_of_files(
                  sourse_img_directory,
                  sourse_img_extension)
    for description_path in description_path_list:
        d_name = get_file_name_from_full_path(description_path)
        i = 0
        for img_path in img_path_list:
            if d_name == get_file_name_from_full_path(img_path):
                d_json = create_product_json(description_path, img_path)
                upload_description_to_the_server(d_json, server_url)
                i = 1
                break
        if i == 0:
            d_json == create_product_json(description_path, "")
            upload_description_to_the_server(d_json, server_url)

def main():
    sourse_description_directory = "./supplier-data/descriptions"
    sourse_description_extension = "*.txt"
    sourse_img_directory = "./supplier-data/images"
    sourse_img_extension = "*.jpeg"
    server_url = "http://[linux-instance-external-IP]/fruits"
    upload_all_descriptions_from_a_folder(sourse_description_directory,
                                          sourse_description_extension,
                                          sourse_img_directory,
                                          sourse_img_extension,
                                          server_url)


if __name__ == '__main__':
    main()
