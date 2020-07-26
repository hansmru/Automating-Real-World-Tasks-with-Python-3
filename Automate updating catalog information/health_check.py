#!/usr/bin/env python3

import psutil,shutil,socket,emails

def error_mail(sub):
	sender = "automation@example.com"
	receipient = "student-02-5fcba15d24c9@example.com"
	subject=sub
	body="Please check your system and resolve the issue as soon as possible."
	message=emails.generate_error_email(sender,receipent,subject,body)
	emails.send_email(message)

def check_cpu_usage():
	usage=psutil.cpu_percent(1)
	if usage>80:
		sub="Error - CPU usage is over 80%"
		error_mail(sub)

def check_disk_usage():
	du=shutil.disk_usage("/")
	free=du.free/du.total*100
	if free<20:
		sub="Error - Available disk space is less than 20%"
		error_mail(sub)

def check_mem():
	memory=dict(psutil.virtual_memory()._asdict())["available"]
	available_mem=(memory/1024)/1024
	if available_mem<500:
		sub="Error - Available memory is less than 500MB"
		error_mail(sub)

def check_host():
	ip=socket.gethostbyname("localhost")
	if ip!="127.0.0.1":
		sub="Error - localhost cannot be resolved to 127.0.0.1"
		error_mail(sub)

if __name__ == "__main__":
	check_cpu_usage()
	check_disk_usage()
	check_mem()
	check_host()