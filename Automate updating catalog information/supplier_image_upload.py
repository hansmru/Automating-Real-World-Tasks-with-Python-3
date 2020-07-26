#!/usr/bin/env python3
import requests
import os

url="http://localhost/upload/"
image_dir="/home/student-02-5fcba15d24c9/supplier-data/images/"

for images in os.listdir(image_dir):
	if not images.startswith(".") and "jpeg" in images:
		image_path=image_dir+images
		with open(image_path,"rb") as opened:
			r=requests.post(url,files={"file":opened})