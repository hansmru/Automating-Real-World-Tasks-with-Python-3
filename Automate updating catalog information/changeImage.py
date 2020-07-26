#!/usr/bin/env python3
import os
from PIL import Image

image_dir="/home/student-02-5fcba15d24c9/supplier-data/images/"

for images in os.listdir(image_dir):
	if not images.startswith(".") and "tiff" in images:
		image_path=image_dir+images
		new_path=os.path.splitext(image_path)[0]
		img=Image.open(image_path)
		img.convert("RGB").resize((600,400)).save(new_path+".jpg","JPEG")