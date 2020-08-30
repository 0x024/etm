# -*- coding:utf-8 -*-
import os
import json
from subprocess import Popen,PIPE
key="ca9b9b6c0f179eb5c62281bd913eec94"

pwd=os.getcwd()



def get_location(address):
	result_raw=Popen('curl -X GET "http://restapi.amap.com/v3/geocode/geo?address=%s&output=JSON&key=%s"'%(address,key),shell=True,stdout=PIPE)
	result=(result_raw.stdout.read()).decode('utf-8')
	result=json.loads(result)
	print (result)
	formatted_address=result["geocodes"][0]["formatted_address"]
	country=result["geocodes"][0]["country"]
	province=result["geocodes"][0]["province"]
	city=result["geocodes"][0]["city"]
	citycode=result["geocodes"][0]["citycode"]
	district=result["geocodes"][0]["district"]
	street=result["geocodes"][0]["street"]
	number=result["geocodes"][0]["number"]
	adcode=result["geocodes"][0]["adcode"]
	lng=result["geocodes"][0]["location"].split(",")[0]
	lat=result["geocodes"][0]["location"].split(",")[1]


get_location("郑州东站")