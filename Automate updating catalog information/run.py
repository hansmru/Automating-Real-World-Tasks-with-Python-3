#! /usr/bin/env python3
import os
import requests
import json

url = "http://localhost/fruits/"
description_files='/home/student-02-5fcba15d24c9/supplier-data/descriptions/'

for descriptions_name in os.listdir(description_files):
	if not descriptions_name.startswith(".") and "txt" in descriptions_name:
		descriptions_path=description_files+descriptions_name
		image_path=descriptions_name.strip(".txt")+".jpeg"

		with open(descriptions_path) as f:
			data=f.readlines()
			name=data[0].strip("\n")
			weight=int(data[1].strip("\n").strip("lbs"))
			descrip=data[2].strip("\n")

			fruits_catalog={"name":name,"weight":weight,"description":descrip.replace(u'\xa0', u''),"image_name":image_path}
			json_file=json.dumps(fruits_catalog)
			header = {'Content-Type': 'application/json'}

			response=requests.post(url,headers=header,data=json_file)
			print(response.reason)