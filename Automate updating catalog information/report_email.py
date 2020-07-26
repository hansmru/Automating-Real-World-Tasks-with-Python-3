#! /usr/bin/env python3

import os,reports
import emails
import glob
from datetime import date

date=date.today()
title="Processed Update on {}".format(date)
text_files=glob.glob("/home/student-02-5fcba15d24c9/supplier-data/descriptions/*.txt")
text_list=[]

for files in text_files:
	with open(files,"r") as f:
		reader=f.read().split("\n")
		text_list.append(reader)

parag=""
for fields in text_list:
	msg=""
	msg="Name: {}<br/> Weight: {}<br/><br/>".format(fields[0],fields[1])
	parag=parag+msg

if __name__ == "__main__":
	sender="automation@example.com"
	receipent="student-02-5fcba15d24c9@example.com"
	subject="Upload Completed - Online Fruit Store"
	body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	attachment="/tmp/processed.pdf"

	reports.generate_report("/tmp/processed.pdf",title,parag)
	message=emails.generate_email(sender,receipent,subject,body,attachment)
	emails.send_email(message)
