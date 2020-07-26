#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender,receipent,subject,body,attachment):
	message=email.message.EmailMessage()
	message["From"] = sender
	message["To"] = receipent
	message["Subject"] = subject
	message.set_content(body)
	attachment_filename = os.path.basename(attachment)
	mime_type, _ = mimetypes.guess_type(attachment)
	mime_type, mime_subtype = mime_type.split('/', 1)

	with open(attachment,"rb") as a:
		message.add_attachment(a.read(),maintype=mime_type,subtype=mime_subtype,filename=attachment)
		return message

def generate_error_email(sender,receipent,subject,body):
	message=email.message.EmailMessage()
	message["From"] = sender
	message["To"] = receipent
	message["Subject"] = subject
	message.set_content(body)

	return message


def send_email(message):
	mail_server = smtplib.SMTP('localhost')
	mail_server.send_message(message)
	mail_server.quit()