#!/usr/bin/env python3

from PIL import Image
import os
import fnmatch
import time

def get_list_of_files_from_directory(sourse_directory, extension):
    """
    Returns a sorted list of files with a specified extension from
    the sourse sourse_directory
    """
    file_list = fnmatch.filter(os.listdir(sourse_directory), extension)
    file_list.sort()
    return file_list

def convert_save_img(img_name, sourse_directory, target_directory,
                     img_format, img_size, img_extension):
    """
    Converts an image from a sourse_directory to a specified size and format and
    saves it into target_directory with img_extension
    """
    img = Image.open(sourse_directory + "/" + img_name)
    #Get the file name without extension
    img_name = os.path.splitext(img_name)[0]
    #Convert image into desired format
    img = img.resize(img_size).convert(img_format)
    #Save image with the desired extension
    img.save(target_directory + "/" + img_name + "." + img_extension,
             img_extension, quality=100)
    img.close()

def convert_img(sourse_directory, target_directory, source_img_extension,
                img_format, img_size, img_extension):
    """
    Converts all images from sourse_directory with source_img_extension to
    a specified size and format and saves it into target_directory
    """
    img_list = get_list_of_files_from_directory(sourse_directory,
                                                source_img_extension)
    for img_name in img_list:
        convert_save_img(img_name, sourse_directory,
                         target_directory, img_format, img_size, img_extension)

def main():
    sourse_directory = "./supplier-data/images"
    target_directory = "./supplier-data/images"
    source_img_extension = "*.tiff"
    img_extension = "jpeg"
    img_format = "RGB"
    img_size = (600, 400)
    start_time = time.time()
    convert_img(sourse_directory,target_directory, source_img_extension,
                img_format, img_size, img_extension)
    print("--- %s seconds ---" % (time.time()-start_time))

if __name__ == '__main__':
    main()
