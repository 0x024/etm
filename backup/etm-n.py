import sqlite3
import os,email,imaplib
from email.parser import BytesParser
from email.utils import parseaddr 
from lxml import etree
import time
import xml.etree.ElementTree as ET
import time
import datetime

aaaa=1


host = 'imap.qq.com'
user = '97073966@qq.com' 
passwd = 'feaybkuahvcacajc'
raw_conn = imaplib.IMAP4_SSL(host) 
raw_conn.login(user,passwd) 
raw_conn.select()
type,data=raw_conn.search(None,'ALL')
email_list=data[0].split()

def decode_str(s):
	try:
		subject=email.header.decode_header(s)
	except:
		return None
	sub_bytes=subject[0][0]
	sub_charset=subject[0][1]
	if None==sub_charset:
		subject=sub_bytes
	elif 'unknown-8bit'==sub_charset:
		subject=str(sub_bytes,'utf-8')
	else:
		subject=str(sub_bytes,sub_charset)
	return subject

def get_transfer_v1(content):
	a1=content.replace('&nbsp;','')
	a2=a1.replace('<a <a ','<a ')
	a3=a2.replace('(<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a4=a3.replace('（<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a5=a4.replace('（<a href="http://www.12306.cn">12306.cn</a>)','')
	a6=a5.replace('(<a href="http://www.12306.cn">12306.cn</a>)','')
	tree=etree.HTML(a6)
	contents=tree.xpath('//text()')
	''.join(contents)
	line_chick=contents[2].replace("\n",'')
	list_chick=line_chick.split('，')
	#print (line_chick)
	order_type=list_chick[0]
	if'购买' in order_type :
		order_count=int(list_chick[0][-4])
		if order_count==2:
			print ('!!!!!!!!!!!!!!!!!!!!!!!!!')
		count =1
		while count < order_count+1:

			line_detail=contents[count+2].replace("\n",'')
			list_chick=line_chick.split('，')
			print(list_chick)
			if ',' in line_detail:
				list_detail=line_detail.split(',')
			elif '，' in line_detail:
				list_detail=line_detail.split('，')
			print (list_detail)
			print ("购买")
			purchaser='张文'
			print(purchaser)
			order_no=list_chick[2][4:].split('。')[0]
			print(order_no)
			order_date=list_chick[0][2:13]
			print (order_date)
			order_price=list_chick[1][4:]
			print (order_price)
			order_type="购买"
			print (order_type)
			passenger=list_detail[0].split('.')[1]
			print (passenger)
			train_date=list_detail[1][:-1]
			print (train_date)
			train_price=list_detail[6][2:]
			print (train_price)
			train_no=list_detail[3].replace("次列车",'')
			print (train_no)
			train_type=list_detail[3][0]
			if train_type.isdigit():
				print ("normla")
			else:
				print (train_type)
			start_station=list_detail[2].split('—')[0]
			print (start_station)
			stop_station=list_detail[2].split('—')[1]
			print (stop_station)
			sit_row=list_detail[4].split("车")[0]
			print (sit_row)
			sit_no=list_detail[4].split("车")[1].split("号")[0]
			print (sit_no)
			sit_type=list_detail[5]
			print (sit_type)
			if sit_type=="硬卧":
				sit_flow=list_detail[4][-2]
				print (sit_flow)
			count=count+1
			


	elif '退票' in order_type:
		line_detail=contents[3].replace("\n",'')
		list_chick=line_chick.split('，')
		print(list_chick)
		if ',' in line_detail:
			list_detail=line_detail.split(',')
		elif '，' in line_detail:
			list_detail=line_detail.split('，')
		print (list_detail)
		print ("退票")
		purchaser='张文'
		print(purchaser)
		order_no=list_chick[1].split('。')[0][5:]
		print(order_no)
		order_date=list_chick[0][2:13]
		print (order_date)
		#order_price=list_chick[1][4:]
		#print (order_price)
		order_type="退票"
		print (order_type)
		passenger=list_detail[0]
		print (passenger)
		train_date=order_date[0:5]+list_detail[1]
		print (train_date)
		train_price=list_detail[6][2:]
		print (train_price)
		train_no=list_detail[3].replace("次列车",'')
		print (train_no)
		train_type=list_detail[3][0]
		if train_type.isdigit():
			print ("normla")
		else:
			print (train_type)
		start_station=list_detail[2].split('—')[0]
		print (start_station)
		stop_station=list_detail[2].split('—')[1]
		print (stop_station)
		sit_row=list_detail[4].split("车")[0].replace(" ","")
		print (sit_row)
		sit_no=list_detail[4].split("车")[1].split("号")[0]
		print (sit_no)
		sit_type=list_detail[5]
		print (sit_type)
		transfer_fee=list_detail[7][3:]
		print (transfer_fee)
		drawback_fee=list_detail[8][4:]
		print (drawback_fee)
		if sit_type=="硬卧":
			sit_flow=list_detail[4][-2]
			print (sit_flow)

	elif  '改签' in order_type :
		line_detail=contents[3].replace("\n",'')
		list_chick=line_chick.split('，')
		print(list_chick)
		if ',' in line_detail:
			list_detail=line_detail.split(',')
		elif '，' in line_detail:
			list_detail=line_detail.split('，')
		print (list_detail)
		print ('改签')
		purchaser='张文'
		print(purchaser)
		order_no=list_chick[2].split('。')[1][4:]
		print(order_no)
		order_date=list_chick[0][2:13]
		print (order_date)
		order_price=list_chick[1][7:]
		print (order_price)
		order_type="改签"
		print (order_type)
		passenger=list_detail[0].split('.')[1]
		print (passenger)
		train_date=list_detail[1][:-1]
		print (train_date)
		train_price=list_detail[6][2:]
		print (train_price)
		train_no=list_detail[3].replace("次列车",'')
		print (train_no)
		train_type=list_detail[3][0]
		if train_type.isdigit():
			print ("normla")
		else:
			print (train_type)
		start_station=list_detail[2].split('—')[0]
		print (start_station)
		stop_station=list_detail[2].split('—')[1]
		print (stop_station)
		sit_row=list_detail[4].split("车")[0]
		print (sit_row)
		sit_no=list_detail[4].split("车")[1].split("号")[0]
		print (sit_no)
		sit_type=list_detail[5]
		print (sit_type)
		if sit_type=="硬卧":
			sit_flow=list_detail[4][-2]
			print (sit_flow)

	#print(list_chick)
	#print (list_detail)
def get_transfer_v2(content):
	a1=content.replace('&nbsp;','')
	a2=a1.replace('<a <a ','<a ')
	a3=a2.replace('(<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a4=a3.replace('（<a href="http://www.12306.cn">www.12306.cn</a>)','')
	a5=a4.replace('（<a href="http://www.12306.cn">12306.cn</a>)','')
	a6=a5.replace('(<a href="http://www.12306.cn">12306.cn</a>)','')
	tree=etree.HTML(a6)
	contents=tree.xpath('//text()')
	print (contents)

	line_chick_part1=contents[30].replace("\n",'').replace("\t",'').replace("\t",'')	
	line_chick_part2=contents[32].replace("\n",'').replace("\t",'').replace("\t",'')	
	line_chick_part3=contents[33].replace("\n",'').replace("\t",'').replace("\t",'')	
	print (line_chick_part1)
	print (line_chick_part2)
	print (line_chick_part3)
	order_type=line_chick_part2
	if '购买' in order_type :
		order_count=int(line_chick_part2.split("，")[0][-4])
		if order_count==2:
			print ('!!!!!!!!!!!!!!!!!!!!!!!!!')
		count =1
		while count < order_count+1:

			list_detail=contents[(count*2)+39].replace("\n",'').replace("\r",'').replace("\t",'').split("，")
			print (list_detail)
			print ("购买")
			purchaser='张文'
			print(purchaser)
			order_no=line_chick_part3
			print(order_no)
			order_date=line_chick_part1[2:13]
			print (order_date)
			order_price=line_chick_part2.split("，")[1][4:]
			print (order_price)
			order_type="购买"
			print (order_type)
			passenger=list_detail[0].split('.')[1]
			print (passenger)
			train_date=list_detail[1][:-1]
			print (train_date)
			train_price=list_detail[5][2:]
			print (train_price)
			train_no=list_detail[3].split(",")[0].replace("次列车",'')
			print (train_no)
			train_type=list_detail[3][0]
			if train_type.isdigit():
				print ("normla")
			else:
				print (train_type)
			start_station=list_detail[2].split('-')[0]
			print (start_station)
			stop_station=list_detail[2].split('-')[1]
			print (stop_station)
			sit_row=list_detail[3].split(",")[1].split("车")[0]
			print (sit_row)
			sit_no=list_detail[3].split(",")[1].split("车")[1].replace("号","")
			print (sit_no)
			sit_type=list_detail[4]
			print (sit_type)
			if sit_type=="硬卧":
				sit_flow=list_detail[4][-2]
				print (sit_flow)
			try:
				ticket_entrance=list_detail[6][3:].split("。")[0]
				print (ticket_entrance)
			except IndexError:
				print("qwqww")

			count=count+1
			


	elif '退票' in order_type:
		line_chick_part4=contents[34].replace("\n",'').replace("\t",'').replace("\t",'')
		list_detail=contents[41].replace("\n",'').replace("\r",'').replace("\t",'').split("，")
		print (list_detail)
		print ("退票")
		purchaser='张文'
		print(purchaser)
		order_no=line_chick_part3
		print(order_no)
		order_date=line_chick_part1[2:13]
		print (order_date)
		order_type="退票"
		print (order_type)
		passenger=list_detail[0]
		print (passenger)
		train_date=list_detail[1][2:16]
		print (train_date)
		train_price=list_detail[5][2:]
		print (train_price)
		train_no=list_detail[3].split(",")[0].replace("次列车",'')
		print (train_no)
		train_type=list_detail[3][0]
		if train_type.isdigit():
			print ("normla")
		else:
			print (train_type)
		start_station=list_detail[2].split('-')[0]
		print (start_station)
		stop_station=list_detail[2].split('-')[1]
		print (stop_station)
		sit_row=list_detail[3].split(",")[1].split("车")[0]
		print (sit_row)
		sit_no=list_detail[3].split(",")[1].split("车")[1].split("号")[0]
		print (sit_no)
		sit_type=list_detail[4]
		print (sit_type)
		if sit_type=="硬卧":
			sit_flow=list_detail[3].split(",")[1].split("车")[1].split("号")[1]
			print (sit_flow)
		try:
			ticket_entrance=list_detail[6][3:].split("。")[0]
			print (ticket_entrance)
		except IndexError:
			print("qwqww")

	elif '改签' in order_type:
		list_detail=contents[41].replace("\n",'').replace("\t",'').replace("\r",'').split("，")
		print(list_detail)
		print ('改签')
		purchaser='张文'
		print(purchaser)
		order_no=line_chick_part3
		print(order_no)
		order_date=line_chick_part1[2:13]
		print (order_date)
		order_price=line_chick_part2.split("，")[1][7:]
		print (order_price)
		order_type="改签"
		print (order_type)
		passenger=list_detail[0].split('.')[1]
		print (passenger)
		train_date=list_detail[1][:-1]
		print (train_date)
		train_price=list_detail[5][2:]
		print (train_price)
		train_no=list_detail[3].split(",")[0].replace("次列车",'')
		print (train_no)
		train_type=list_detail[3][0]
		if train_type.isdigit():
			print ("normla")
		else:
			print (train_type)
		start_station=list_detail[2].split('-')[0]
		print (start_station)
		stop_station=list_detail[2].split('-')[1]
		print (stop_station)
		sit_row=list_detail[3].split(",")[1].split("车")[0]
		print (sit_row)
		sit_no=list_detail[3].split(",")[1].split("车")[1].split("号")[0]
		print (sit_no)
		sit_type=list_detail[4]
		print (sit_type)
		if sit_type=="硬卧":
			sit_flow=list_detail[3].split(",")[1].split("车")[1].split("号")[1]
			print (sit_flow)
		try:
			ticket_entrance=list_detail[6][3:].split("。")[0]
			print (ticket_entrance)
		except IndexError:
			print("qwqww")


def get_subject(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	try:
		msg=BytesParser().parsebytes(data[0][1])
		sub=decode_str(msg.get('subject'))
		print(sub)
		return sub
	except TypeError:
		print ('empty-email')
	except UnicodeDecodeError:
		print ('hahah')
def get_from(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	try :
		msg=BytesParser().parsebytes(data[0][1])
		sub=decode_str(msg.get('From'))
		#print (sub)
		return sub

	except TypeError:
		print ('empty-email')
		#print(sub)			
	except UnicodeDecodeError:
		print ('hahah')
def get_date(num):
	type,data=raw_conn.fetch(num,'(RFC822)')
	try :
		msg=BytesParser().parsebytes(data[0][1])
		sub=msg.get('Date')
		#print(sub)
		return sub
	#print(num, decode_str(sub)) 
	except TypeError:
		print ('empty-email')
	except UnicodeDecodeError:
		print ('hahah')

def time_formate(email_time):
	mind_befor_CTS_time='Fri 10 Nov 2017 00:00:00 '
	mind_formate_time=datetime.datetime.strptime(mind_befor_CTS_time,"%a %d %b %Y %H:%M:%S ")
	
	email_recive_CTS_time=email_time.replace("(CST)","").replace(",","").replace(" +0800","")
	email_formate_time=datetime.datetime.strptime(email_recive_CTS_time,"%a %d %b %Y %H:%M:%S ")
	if email_formate_time >= mind_formate_time:
		return '2'
	else:
		return '1'
def get_content(num):
	print (num)
	type,data=raw_conn.fetch(num,'(RFC822)')
	email_date=get_date(email_list[int(count)])
	try :
		msg=BytesParser().parsebytes(data[0][1])
		for part in msg.walk():
			if not part.is_multipart():   
				charset = part.get_charset()
				contenttype = part.get_content_type()
				content=part.get_payload(decode=True)
				content=content.decode('GBK')
				temp=time_formate(email_date)
				print(temp)
				if temp=='1':
					print(temp)
					get_transfer_v1(content)
				elif temp=='2':
					print(temp)
					get_transfer_v2(content)

				
				#
				#print (content)

	except TypeError:
		print ('empty-email')
	except UnicodeDecodeError:
		print ('hahah')




'''if __name__ == '__main__':
	for count in email_list:
		#print("VVVVVVVV")
		print(int(count))
		org_addrs=str(get_from(email_list[int(count)]))
		#print (isinstance(org_addrs,str))
		tar_addrs="<12306@rails.com.cn>"
		if tar_addrs in  org_addrs:
			#aaaa=aaaa+1
			print("OOOOOO")
			get_content(email_list[int(count)])
			
			#print ("+++++++++++="+str(aaaa))
			continue'''

if __name__ == '__main__':
	count = 290
	while count < 520:
		print(int(count))
		org_addrs=str(get_from(email_list[int(count)]))
		#print (isinstance(org_addrs,str))
		tar_addrs="<12306@rails.com.cn>"
		if tar_addrs in  org_addrs:
			print("OOOOOO")
			print (count)
			get_content(email_list[int(count)])
		count=count+1
		
		print("******************************")

#
#get_from(email_list[330])
#get_content(email_list[173])

	



				#get_content(email_list[30])`

		




		#print (isinstance(org_addrs,str))
		#if org_addrs==tar_addrs:
		#	print ('222')
		#else:
		#	print("111")

		
	#get_date(email_list[21])
	#get_subject(email_list[21])
	#get_content(email_list[21])
	#get_subject(newlist[3],raw_conn)
		#for part in msg.walk():
		#	if not part.is_multipart():
		#		print(part.get_payload(decode=True).decode('utf-8'))
	#raw_conn.close()
	#raw_conn.logout()