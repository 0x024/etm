import os
import sqlite3

conn =sqlite3.connect('etm.db')
cursor=conn.cursor()
cursor.execute('select * from purchase where train_passenger="张文"')
values=cursor.fetchall()
city_lines=[]
for i in range(len(values)):
	start_station=str(values[i][14])
	start_lng=values[i][15]
	start_lat=values[i][16]
	start_lnglat=start_lng+","+start_lat
	stop_staton=str(values[i][17])
	stop_lng=values[i][18]
	stop_lat=values[i][19]
	stop_lnglat=stop_lng+","+stop_lat
	name=str(start_station+"-"+stop_staton)
	line=str("\""+start_lnglat+"\",\""+stop_lnglat+"\"")
	city_line="{\"name\":\""+name+"\","+"\"line\":["+line+"]}"
	city_lines.append(city_line)

	print (city_lines)
f = open("city_line.js", "a")
f.write("var city_line ="+str(city_lines).replace("'",""))
f.close()
	
#print (values)
cursor.close()
conn.close()
