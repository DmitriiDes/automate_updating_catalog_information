#!/usr/bin/env python3

from email.message import EmailMesage
import os.path
import mimetypes
import smtplib
import getpass

def generate_email(sender, recipient, subject = "", body = "", attachement_path = ""):
    """
    Constructs an email message based on received info with an optional attachement
    """
    message = EmailMessage()
    message["From"] = sender
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)
    if not attachement_path:
        attachement_filename = os.path.basename(attachement_path)
        mime_type, _ = mimetypes.guess_type(attachement_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        with open(attachement_path, "rb") as attachement:
            message.add_attachement(attachement.read(),
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=attachement_filename)
    return message

def send_email(sender, message):
    """
    Log in into mail server and send the message
    """
    mail_server = smtplib.SMTP_SSL(sender)
    mail_pass = getpass.getpass("Email Password: ")
    mail_server.login(sender, mail_pass)
    mail_server.send_message(message)
    mail_server.quit()
