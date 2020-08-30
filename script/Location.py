# -*- coding:utf-8 -*-
import os
import json
import sqlite3
from subprocess import Popen,PIPE
key="ca9b9b6c0f179eb5c62281bd913eec94"
pwd=os.getcwd()
db_pwd=pwd+"/database/etm.db"

print (db_pwd)
conn =sqlite3.connect(db_pwd)
c=conn.cursor()

def get_local(station):
	if "站" not in station:
		station=station+"站"
	c.execute("select * from location where  station='%s'"%(station))
	temp_results = c.fetchall()
	conn.commit()
	#print (temp_results)
	if len(temp_results)==0:
		result_raw=Popen('curl -X GET "http://restapi.amap.com/v3/geocode/geo?address=%s&output=JSON&key=%s"'%(station,key),shell=True,stdout=PIPE)
		result=(result_raw.stdout.read()).decode('utf-8')
		result=json.loads(result)
		#print (result)
		formatted_address=result["geocodes"][0]["formatted_address"]
		country=result["geocodes"][0]["country"]
		province=result["geocodes"][0]["province"]
		city=result["geocodes"][0]["city"]
		try:
			citycode=result["geocodes"][0]["citycode"]
		except KeyError:
			citycode="0000"
		district=result["geocodes"][0]["district"]
		street=result["geocodes"][0]["street"]
		streetnumber=result["geocodes"][0]["number"]
		adcode=result["geocodes"][0]["adcode"]
		lnglat=str(result["geocodes"][0]["location"])
		lng=result["geocodes"][0]["location"].split(",")[0]
		lat=result["geocodes"][0]["location"].split(",")[1]
		c.execute("PRAGMA busy_timeout = 10000")
		conn.commit()
		c.execute("INSERT INTO location (station,formatted_address,country,province,city,citycode,district,street,streetnumber,adcode,lng,lat) \
					VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
					%(station,formatted_address,country,province,city,citycode,district,street,streetnumber,adcode,lng,lat))
		conn.commit()
		c.execute("PRAGMA busy_timeout = 10000")
		conn.commit()

	elif len(temp_results)==1:
		lng=temp_results[0][10]
		lat=temp_results[0][11]
	return (lng,lat)


	'''c.execute("select distinct * from location where  lng='%s'"%(lng))
	temp_results = c.fetchall()
	if len(temp_results)==0:
		c.execute("INSERT INTO location (formatted_address,country,province,station,citycode,district,street,streetnumber,adcode,lng,lat) \
					VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
					%(formatted_address,country,province,station,citycode,district,street,streetnumber,adcode,lng,lat))
	else:
		print ("hahahah")
	conn.commit()
	conn.close()
	return (lng,lat)'''
print(get_local("安阳东"))