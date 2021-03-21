#!/usr/bin/env python3

import datetime
import reports
from supplier_image_upload import get_full_path_list_of_files
from run import convert_txt_description_into_lines
import emails

def get_additional_info(source_directory, file_extension):
    """
    Creates multiline string of name: weight: based on reviews in the folder
    """
    additional_info = ""
    description_path_list = get_full_path_list_of_files(source_directory, file_extension)
    for description_path in description_path_list:
        product_description_lines = convert_txt_description_into_lines(
                                  description_path)
        additional_info += "name:{} \nweight:{}".format(product_description_lines[0], product_description_lines[1])
        additional_info += "\n\n"
    return additional_info

def main():
    #Report related data
    source_description_directory = "./supplier-data/descriptions"
    source_description_extension = "*.txt"
    generated_report_path = "/tmp/"
    report_name = "processed.pdf"
    title = "Processed Update on {}".format(datetime.date.today())
    additional_info = get_additional_info(source_description_directory, source_description_extension)
    report.generate_report(generated_report_path, report_name, title, additional_info)
    #Email related data
    sender = "automation@example.com"
    recipient = "username@example.com" #Replace username with the username given in the Connection Details Panel on the right hand side
    email_subject = "Upload Completed - Online Fruit Store"
    email_body = "All fruits are uploaded to our website successfully. A detailed list is attached to thie email."
    attachement_path = generated_report_path + report_name
    message = emails.generate_email(sender, recipient, email_subject, email_body, attachement_path)
    emails.send_email(sender, message)

if __name__ == '__main__':
    main()
