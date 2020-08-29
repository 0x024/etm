import re
from lxml import etree
import sqlite3
import datetime
import time
from script import Location
from script import Timeformate
conn =sqlite3.connect("/home/ubuntu/Desktop/etm/database/etm.db")
c=conn.cursor()





def get_transfer_v1(content,id):
	a1=content.replace('&nbsp;','')
	a2=a1.replace('<a <a ','<a ')
	a3=a2.replace('(<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a4=a3.replace('（<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a5=a4.replace('（<a href="http://www.12306.cn">12306.cn</a>)','')
	a6=a5.replace('(<a href="http://www.12306.cn">12306.cn</a>)','')
	tree=etree.HTML(a6)
	contents=tree.xpath('//text()')
	#''.join(contents)----
	line_chick=contents[2].replace("\n",'').replace("\r",'')
	list_chick=line_chick.split('，')



	order_type=list_chick[0]
	if  '购买' in order_type :
		print("~~~~~~~~~~~~~~~~~part_2_start~~~~~~~~~~~~~~~~~~~~~~~")
		order_count=int(list_chick[0][-4])
		print ('此订单包含'+str(order_count)+'张车票')
		order_no=list_chick[2][4:].split('。')[0]
		print('订单号:'+str(order_no))
		order_purchaser='张文'
		print('操作人员:'+order_purchaser)
		order_date_o=list_chick[0][2:13].replace("年",'').replace("月",'').replace("日",'')
		print (order_date_o)
		print (isinstance(order_date_o,str))
		order_date=Timeformate.order_time_formate(order_date_o)
		print ('订单日期:'+order_date_o)
		order_price=list_chick[1][4:].replace("元",'')
		print ('订单金额:'+order_price)
		order_type="购买"
		print ('订单状态:'+order_type)
		count =1
		while count < order_count+1:
			line_detail=contents[count+2].replace("\n",'').replace("\r",'')
			if ',' in line_detail:
				list_detail=line_detail.split(',')
			elif '，' in line_detail:
				list_detail=line_detail.split('，')
			print(list_chick)
			print (list_detail)
			print ('第'+str(count)+'张车票信息如下')
			train_passenger=list_detail[0].split('.')[1]
			print ('火车乘客:'+train_passenger)
			train_date_o=list_detail[1][:-1].replace("年",'').replace("月",'').replace("日",'')
			train_date=Timeformate.train_time_formate(train_date_o)
			print ('发车日期:'+train_date_o)
			train_no=list_detail[3].replace("次列车",'')
			print ('火车车次:'+train_no)
			train_price=list_detail[6].split("，")[0][2:].replace("。",'').replace("元",'')
			print ('火车票价:'+train_price)
			train_type=list_detail[3][0]
			if train_type.isdigit():
				train_type='绿皮'
				print ('火车类型:绿皮火车')
			else:
				print ('火车类型:'+train_type)
			start_station=list_detail[2].split('—')[0]
			print ('出发站:'+start_station)
			start_lng=Location.get_local(start_station[0:2])[0]
			print ("经度:"+str(start_lng))
			start_lat=Location.get_local(start_station[0:2])[1]
			print ("维度:"+str(start_lat))
			stop_station=list_detail[2].split('—')[1]
			print ('终点站:'+stop_station)
			stop_lng=Location.get_local(stop_station[0:2])[0]
			print ("经度:"+str(stop_lng))
			stop_lat=Location.get_local(stop_station[0:2])[1]
			print ("维度:"+str(stop_lat))		
			sit_type=list_detail[5]
			print ('座位类型:'+sit_type)
			sit_row=list_detail[4].split("车")[0]
			print ('车厢号:'+sit_row)
			sit_no=list_detail[4].split("车")[1].split("号")[0]
			print ('座位号:'+sit_no)
			c.execute("INSERT INTO purchase (order_id,order_no,order_purchaser,order_date,order_count,order_price,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no) \
				VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
				%(id,order_no,order_purchaser,order_date,order_count,order_price,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no))
			conn.commit()
			try:
				raw_sit=list_detail[4].split("车")[1].split("号")[1]
			except IndexError:
				print ("无座")
			if sit_type=="硬卧":
				if"上" in raw_sit:
					sit_flow='上'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  purchase SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif"中" in raw_sit:
					sit_flow='中'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  purchase SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif "下" in raw_sit:
					sit_flow='下'	
					print ("卧铺位置:"+sit_flow)	
					c.execute("UPDATE  purchase SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()		
			'''if start_station=="郑州东站":
				ticket_entrance=list_detail[6][3:].split("。")[0]
				print ("检票口:"+ticket_entrance)
			else:
				print("非郑州东站，不检测检票口")'''

			#conn.close()
			count=count+1
			print("~~~~~~~~~~~~~~~~~part_2_end~~~~~~~~~~~~~~~~~~~~~~~")

			


	elif '退票' in order_type:
		line_detail=contents[3].replace("\n",'').replace("\r",'')
		if ',' in line_detail:
			list_detail=line_detail.split(',')
		elif '，' in line_detail:
			list_detail=line_detail.split('，')
		print(list_chick)
		print (list_detail)
		print("~~~~~~~~~~~~~~~~~part_2_start~~~~~~~~~~~~~~~~~~~~~~~")
		order_no=list_chick[1].split('。')[0][5:]
		print('订单号:'+str(order_no))
		order_purchaser='张文'
		print('操作人员:'+order_purchaser)
		order_date_o=list_chick[0][2:13].replace("年",'').replace("月",'').replace("日",'')
		order_date=Timeformate.order_time_formate(order_date_o)
		print (order_date)
		print ('订单日期:'+order_date_o)
		order_type="退票"
		print ('订单状态:'+order_type)
		train_passenger=list_detail[0]
		print ('退票乘客:'+train_passenger)
		train_date_o=order_date_o[0:4]+list_detail[1].replace("年",'').replace("月",'').replace("日",'')
		train_date=Timeformate.train_time_formate(train_date_o)
		print ('发车日期:'+train_date_o)
		train_no=list_detail[3].replace("次列车",'')
		print ('火车车次:'+train_no)
		train_price=list_detail[6][2:].replace("元",'')
		print ('原始票价:'+train_price)
		transfer_fee=list_detail[7][3:].replace("元",'')
		print ('退手续费:'+transfer_fee)
		drawback_fee=list_detail[8][4:].replace("。",'').replace("元",'')
		print ('应退金额:'+drawback_fee)
		train_type=list_detail[3][0]
		if train_type.isdigit():
			train_type='绿皮'
			print ('火车类型:绿皮火车')
		else:
			print ('火车类型:'+train_type)
		start_station=list_detail[2].split('—')[0]
		print ('出发站:'+start_station)
		start_lng=Location.get_local(start_station[0:2])[0]
		print ("经度:"+str(start_lng))
		start_lat=Location.get_local(start_station[0:2])[1]
		print ("维度:"+str(start_lat))
		stop_station=list_detail[2].split('—')[1]
		print ('终点站:'+stop_station)
		stop_lng=Location.get_local(stop_station[0:2])[0]
		print ("经度:"+str(stop_lng))
		stop_lat=Location.get_local(stop_station[0:2])[1]
		print ("维度:"+str(stop_lat))
		sit_type=list_detail[5]
		print ('座位类型:'+sit_type)
		sit_row=list_detail[4].split("车")[0].replace(" ","")
		print ('车厢号:'+sit_row)
		sit_no=list_detail[4].split("车")[1].split("号")[0]
		print ('座位号:'+sit_no)
		c.execute("INSERT INTO Refund (order_id,order_no,order_purchaser,order_date,order_type,train_passenger,train_date,train_no,train_price,transfer_fee,drawback_fee,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no) \
			VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
			%(id,order_no,order_purchaser,order_date,order_type,train_passenger,train_date,train_no,train_price,transfer_fee,drawback_fee,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no))
		conn.commit()
		try:
			raw_sit=list_detail[4].split("车")[1].split("号")[1]
		except IndexError:
			print ("无座")
		if sit_type=="硬卧":
			if"上" in raw_sit:
				sit_flow='上'
				print ("卧铺位置:"+sit_flow)
				c.execute("UPDATE  Refund SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
				conn.commit()
			elif"中" in raw_sit:
				sit_flow='中'
				print ("卧铺位置:"+sit_flow)
				c.execute("UPDATE  Refund SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
				conn.commit()
			elif "下" in raw_sit:
				sit_flow='下'	
				print ("卧铺位置:"+sit_flow)	
				c.execute("UPDATE  Refund SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
				conn.commit()
		'''if start_station=="郑州东站":
			ticket_entrance=list_detail[6][3:].split("。")[0]
			print ("检票口:"+ticket_entrance)
		else:
			print("非郑州东站，不检测检票口")'''
		print("~~~~~~~~~~~~~~~~~part_2_end~~~~~~~~~~~~~~~~~~~~~~~")

	elif  '改签' in order_type :
		order_count=int(list_chick[0][-2])
		print ('此订单包含'+str(order_count)+'张车票')
		order_no=list_chick[2].split('。')[1][4:]
		print('订单号:'+str(order_no))
		order_purchaser='张文'
		print('操作人员:'+order_purchaser)
		order_date_o=list_chick[0][2:13].replace("年",'').replace("月",'').replace("日",'')
		order_date=Timeformate.order_time_formate(order_date_o)
		print ('订单日期:'+order_date_o)
		order_type="退票"
		print ('订单状态:'+order_type)
		count =1
		while count < order_count+1:
			line_detail=contents[count+2].replace("\n",'').replace("\r",'')
			if ',' in line_detail:
				list_detail=line_detail.split(',')
			elif '，' in line_detail:
				list_detail=line_detail.split('，')
			if ',' in line_detail:
				list_detail=line_detail.split(',')
			elif '，' in line_detail:
				list_detail=line_detail.split('，')
			print(list_chick)
			print (list_detail)
			print("~~~~~~~~~~~~~~~~~part_2_start~~~~~~~~~~~~~~~~~~~~~~~")
			print ('第'+str(count)+'张车票信息如下')
			train_passenger=list_detail[0].split('.')[1]
			print ('改签乘客:'+train_passenger)
			train_date_o=order_date_o[0:4]+list_detail[1].replace("开",'').replace("年",'').replace("月",'').replace("日",'')
			train_date=Timeformate.train_time_formate(train_date_o)
			print ('发车日期:'+train_date_o)
			train_no=list_detail[3].replace("次列车",'')
			print ('火车车次:'+train_no)
			train_price=list_detail[6][2:].replace("。",'').replace("元",'')
			print ('火车票价:'+train_price)
			train_type=list_detail[3][0]
			if train_type.isdigit():
				train_type='绿皮'
				print ('火车类型:绿皮火车')
			else:
				print ('火车类型:'+train_type)
			start_station=list_detail[2].split('—')[0]
			print ('出发站:'+start_station)
			start_lng=Location.get_local(start_station[0:2])[0]
			print ("经度:"+str(start_lng))
			start_lat=Location.get_local(start_station[0:2])[1]
			print ("维度:"+str(start_lat))
			stop_station=list_detail[2].split('—')[1]
			print ('终点站:'+stop_station)
			stop_lng=Location.get_local(stop_station[0:2])[0]
			print ("经度:"+str(stop_lng))
			stop_lat=Location.get_local(stop_station[0:2])[1]
			print ("维度:"+str(stop_lat))
			sit_type=list_detail[5]
			print ('座位类型:'+sit_type)
			sit_row=list_detail[4].split("车")[0].replace(" ","")
			print ('车厢号:'+sit_row)
			sit_no=list_detail[4].split("车")[1].split("号")[0]
			print ('座位号:'+sit_no)
			c.execute("INSERT INTO change (order_id,order_no,order_purchaser,order_date,order_count,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no) \
				VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
				%(id,order_no,order_purchaser,order_date,order_count,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no))
			conn.commit()
			try:
				raw_sit=list_detail[4].split("车")[1].split("号")[1]
			except IndexError:
				print ("无座")
			if sit_type=="硬卧":
				if"上" in raw_sit:
					sit_flow='上'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  change SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif"中" in raw_sit:
					sit_flow='中'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  change SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif "下" in raw_sit:
					sit_flow='下'	
					print ("卧铺位置:"+sit_flow)	
					c.execute("UPDATE  change SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
			'''if start_station=="郑州东站":
				ticket_entrance=list_detail[6][3:].split("。")[0]
				print ("检票口:"+ticket_entrance)
			else:
				print("非郑州东站，不检测检票口")'''
			count=count+1
			print("~~~~~~~~~~~~~~~~~part_2_end~~~~~~~~~~~~~~~~~~~~~~~")


	#print(list_chick)
	#print (list_detail)
def get_transfer_v2(content,id):
	a1=content.replace('&nbsp;','')
	a2=a1.replace('<a <a ','<a ')
	a3=a2.replace('(<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a4=a3.replace('（<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a5=a4.replace('（<a href="http://www.12306.cn">12306.cn</a>)','')
	a6=a5.replace('(<a href="http://www.12306.cn">12306.cn</a>)','')
	tree=etree.HTML(a6)
	contents=tree.xpath('//text()')
	#print (contents)

	line_chick_part1=contents[30].replace("\n",'').replace("\t",'').replace("\t",'')	
	line_chick_part2=contents[32].replace("\n",'').replace("\t",'').replace("\t",'')	
	line_chick_part3=contents[33].replace("\n",'').replace("\t",'').replace("\t",'')	
	print (line_chick_part1)
	print (line_chick_part2)
	print (line_chick_part3)
	order_type=line_chick_part2
	if '购买' in order_type :
		print("~~~~~~~~~~~~~~~~~part_2_start~~~~~~~~~~~~~~~~~~~~~~~")
		#order_count=int(line_chick_part2.split("，")[0][-4])
		order_count=int(re.findall("\d+",line_chick_part2.split("，")[0])[0])
		print ('此订单包含'+str(order_count)+'张车票')
		order_no=line_chick_part3
		print("订单号:"+order_no)
		order_purchaser='张文'
		print("操作人员:"+order_purchaser)
		order_date_o=line_chick_part1[2:13].replace("年",'').replace("月",'').replace("日",'')
		order_date=Timeformate.order_time_formate(order_date_o)
		print("订单日期:"+order_date_o)
		order_price=line_chick_part2.split("，")[1][4:]
		print("订单金额:"+order_price)
		order_type="购买"
		print("订单状态:"+order_type)
		count =1
		while count < order_count+1:
			list_detail=contents[(count*2)+39].replace("\n",'').replace("\r",'').replace("\t",'').split("，")
			print (list_detail)
			print ('第'+str(count)+'张车票信息如下')
			train_passenger=list_detail[0].split('.')[1]
			print ("火车乘客:"+train_passenger)
			train_date_o=list_detail[1][:-1].replace("年",'').replace("月",'').replace("日",'')
			train_date=Timeformate.train_time_formate(train_date_o)
			print ("发车日期:"+train_date_o)
			train_no=list_detail[3].split(",")[0].replace("次列车",'')
			print ("火车车次:"+train_no)
			train_price=list_detail[5][2:].replace("。",'')
			print ("火车票价:"+train_price)
			train_type=list_detail[3][0]
			if train_type.isdigit():
				train_type='绿皮'
				print ('火车类型:绿皮火车')
			else:
				print ('火车类型:'+train_type)
			start_station=list_detail[2].split('-')[0]
			print ("出发站:"+start_station)
			start_lng=Location.get_local(start_station[0:2])[0]
			print ("经度:"+str(start_lng))
			start_lat=Location.get_local(start_station[0:2])[1]
			print ("维度:"+str(start_lat))
			stop_station=list_detail[2].split('-')[1]
			print ("终点站:"+stop_station)
			stop_lng=Location.get_local(stop_station[0:2])[0]
			print ("经度:"+str(stop_lng))
			stop_lat=Location.get_local(stop_station[0:2])[1]
			print ("维度:"+str(stop_lat))
			sit_type=list_detail[4]
			print ("座位类型:"+sit_type)
			sit_row=list_detail[3].split(",")[1].split("车")[0]
			print ("车厢号:"+sit_row)
			sit_no=list_detail[3].split(",")[1].split("车")[1].split("号")[0]
			print ("座位号:"+sit_no)
			c.execute("INSERT INTO purchase (order_id,order_no,order_purchaser,order_date,order_count,order_price,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no) \
				VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
				%(id,order_no,order_purchaser,order_date,order_count,order_price,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no))
			conn.commit()
			try:			
				raw_sit=list_detail[3].split(",")[1].split("车")[1].split("号")[1]
			except IndexError:
				print ("无座")
			if sit_type=="硬卧":
				if"上" in raw_sit:
					sit_flow='上'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  purchase SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()					
				elif"中" in raw_sit:
					sit_flow='中'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  purchase SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif "下" in raw_sit:
					sit_flow='下'	
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  purchase SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
			if '郑州东' in start_station:

				try:
					ticket_entrance=list_detail[6][3:].split("。")[0].replace("：",'')
					print ("检票口:"+ticket_entrance)
					c.execute("UPDATE  purchase SET ticket_entrance='%s' WHERE  order_no='%s'"%(ticket_entrance,order_no))

				except IndexError:
					print ("虽是郑州东站，但确实没标记进站口")
			else:
				print("非郑州东站，不检测检票口")
			count=count+1
			print("~~~~~~~~~~~~~~~~~part_2_end~~~~~~~~~~~~~~~~~~~~~~~")


	elif '退票' in order_type:
		line_chick_part4=contents[34].replace("\n",'').replace("\t",'').replace("\t",'')
		list_detail=contents[41].replace("\n",'').replace("\r",'').replace("\t",'').split("，")
		print (list_detail)
		order_no=line_chick_part3
		print("订单号:"+order_no)
		order_purchaser='张文'
		print("操作人员:"+order_purchaser)
		order_date_o=line_chick_part1[2:13].replace("年",'').replace("月",'').replace("日",'')
		order_date=Timeformate.order_time_formate(order_date_o)
		print ("订单日期:"+order_date_o)
		order_type="退票"
		print ("订单状态:"+order_type)
		train_passenger=list_detail[0].replace("1.",'')
		print ("退票乘客:"+train_passenger)
		train_date_o=list_detail[1][:16].replace("年",'').replace("月",'').replace("日",'')
		print (train_date_o)
		train_date=Timeformate.train_time_formate(train_date_o)
		print ("发车日期:"+train_date_o)
		train_no=list_detail[3].split(",")[0].replace("次列车",'')
		print ("火车车次:"+train_no)
		train_price=list_detail[5][2:].replace("。",'')
		print ("原始票价:"+train_price)
		
		try:
			transfer_fee=list_detail[6][3:].replace("。",'')
			print ('退手续费:'+transfer_fee)
			drawback_fee=list_detail[7][4:].replace("。",'')
			print ('应退金额:'+drawback_fee)
		except IndexError:
			print ("票据内容不标准，忽略")
			transfer_fee="票据内容不标准"
			drawback_fee="票据内容不标准"
		train_type=list_detail[3][0]
		if train_type.isdigit():
			train_type='绿皮'
			print ('火车类型:绿皮火车')
		else:
			print ('火车类型:'+train_type)
		start_station=list_detail[2].split('-')[0]
		print ("出发站:"+start_station)
		start_lng=Location.get_local(start_station[0:2])[0]
		print ("经度:"+str(start_lng))
		start_lat=Location.get_local(start_station[0:2])[1]
		print ("维度:"+str(start_lat))
		stop_station=list_detail[2].split('-')[1]
		print ("终点站:"+stop_station)
		stop_lng=Location.get_local(stop_station[0:2])[0]
		print ("经度:"+str(stop_lng))
		stop_lat=Location.get_local(stop_station[0:2])[1]
		print ("维度:"+str(stop_lat))
		sit_row=list_detail[3].split(",")[1].split("车")[0]
		print ("车厢号:"+sit_row)
		sit_no=list_detail[3].split(",")[1].split("车")[1].split("号")[0]
		print ("座位号:"+sit_no)
		sit_type=list_detail[4]
		print ("座位类型:"+sit_type)
		c.execute("INSERT INTO Refund (order_id,order_no,order_purchaser,order_date,order_type,train_passenger,train_date,train_no,train_price,transfer_fee,drawback_fee,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no) \
			VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
			%(id,order_no,order_purchaser,order_date,order_type,train_passenger,train_date,train_no,train_price,transfer_fee,drawback_fee,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no))
		conn.commit()
		try:
			raw_sit=list_detail[3].split(",")[1].split("车")[1].split("号")[1]
		except IndexError:
			print ("无座")
		if sit_type=="硬卧":
			if"上" in raw_sit:
				sit_flow='上'
				print ("卧铺位置:"+sit_flow)
				c.execute("UPDATE  Refund SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
				conn.commit()
			elif"中" in raw_sit:
				sit_flow='中'
				print ("卧铺位置:"+sit_flow)
				c.execute("UPDATE  Refund SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
				conn.commit()
			elif "下" in raw_sit:
				sit_flow='下'	
				print ("卧铺位置:"+sit_flow)
				c.execute("UPDATE  Refund SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
				conn.commit()
		print("~~~~~~~~~~~~~~~~~part_2_end~~~~~~~~~~~~~~~~~~~~~~~")

	elif '改签' in order_type:
		print("~~~~~~~~~~~~~~~~~part_2_start~~~~~~~~~~~~~~~~~~~~~~~")
		order_count=int(re.findall("\d+",line_chick_part2.split("，")[0])[0])
		print ('此订单包含'+str(order_count)+'张车票')
		order_no=line_chick_part3
		print("订单号:"+order_no)
		order_purchaser='张文'
		print("操作人员:"+order_purchaser)
		order_date_o=line_chick_part1[2:13].replace("年",'').replace("月",'').replace("日",'')
		order_date=Timeformate.order_time_formate(order_date_o)
		print ("订单日期:"+order_date_o)
		order_type="改签"
		print ("订单状态:"+order_type)
		order_price=line_chick_part2.split("，")[1][7:]
		print ("订单金额:"+order_price)
		count =1
		while count < order_count+1:
			list_detail=contents[(count*2)+39].replace("\n",'').replace("\t",'').replace("\r",'').split("，")
			print(list_detail)
			train_passenger=list_detail[0].split('.')[1]
			if '等价' in line_chick_part2:
				print("车票差价:0元")
			else:
				print("车票差价:111111元")
			print ("改签乘客:"+train_passenger)
			train_date_o=list_detail[1][:-1].replace("年",'').replace("月",'').replace("日",'')
			train_date=Timeformate.train_time_formate(train_date_o)
			print ("发车日期:"+train_date_o)
			train_price=list_detail[5][2:].replace("。",'')
			train_no=list_detail[3].split(",")[0].replace("次列车",'')
			print ("火车车次:"+train_no)
			print ("火车票价:"+train_price)
			train_type=list_detail[3][0]
			if train_type.isdigit():
				train_type='绿皮'
				print ('火车类型:绿皮火车')
			else:
				print ('火车类型:'+train_type)
			start_station=list_detail[2].split('-')[0]
			print ("出发站:"+start_station)
			start_lng=Location.get_local(start_station[0:2])[0]
			print ("经度:"+str(start_lng))
			start_lat=Location.get_local(start_station[0:2])[1]
			print ("维度:"+str(start_lat))
			stop_station=list_detail[2].split('-')[1]
			print ("终点站:"+stop_station)
			stop_lng=Location.get_local(stop_station[0:2])[0]
			print ("经度:"+str(stop_lng))
			stop_lat=Location.get_local(stop_station[0:2])[1]
			print ("维度:"+str(stop_lat))
			sit_row=list_detail[3].split(",")[1].split("车")[0]
			sit_type=list_detail[4]
			print ("座位类型:"+sit_type)
			print ("车厢号:"+sit_row)
			sit_no=list_detail[3].split(",")[1].split("车")[1].split("号")[0]
			print ("座位号:"+sit_no)
			c.execute("INSERT INTO change (order_id,order_no,order_purchaser,order_date,order_count,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no) \
				VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
				%(id,order_no,order_purchaser,order_date,order_count,order_type,train_passenger,train_date,train_no,train_price,train_type,start_station,start_lat,start_lng,stop_station,stop_lat,stop_lng,sit_type,sit_row,sit_no))
			conn.commit()
			try:
				raw_sit=list_detail[3].split(",")[1].split("车")[1].split("号")[1]
			except IndexError:
				print ("无座")
			if sit_type=="硬卧":
				if"上" in raw_sit:
					sit_flow='上'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  change SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif"中" in raw_sit:
					sit_flow='中'
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  change SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()
				elif "下" in raw_sit:
					sit_flow='下'	
					print ("卧铺位置:"+sit_flow)
					c.execute("UPDATE  change SET sit_flow='%s' WHERE  order_no='%s'"%(sit_flow,order_no))
					conn.commit()


			if '郑州东' in start_station:
				try:
					ticket_entrance=list_detail[6][3:].split("。")[0]
					print ("检票口:"+ticket_entrance)
				except IndexError:
					print ("虽是郑州东站，但确实没标记进站口")

			else:
				print("非郑州东站，不检测检票口")
			count=count+1
			print("~~~~~~~~~~~~~~~~~part_2_end~~~~~~~~~~~~~~~~~~~~~~~")
