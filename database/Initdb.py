import sqlite3
import os
pwd=os.getcwd()
db_pwd=pwd+"/database/etm.db"
def init_etmdb(choose):
	if choose==0:
		build_etmdb()
	elif choose==1:
		if  os.path.exists(db_pwd):
			clean_etmdb()	
			build_etmdb()
		else:
			build_etmdb()


def clean_etmdb():
	conn =sqlite3.connect(db_pwd)
	c = conn.cursor()
	c.execute('DROP TABLE IF EXISTS "change";')
	c.execute('DROP TABLE IF EXISTS "etm_aio";')
	c.execute('DROP TABLE IF EXISTS "purchase";')
	c.execute('DROP TABLE IF EXISTS "Refund";')
	conn.commit()
	conn.close()


def build_etmdb():
	conn =sqlite3.connect(db_pwd)
	c = conn.cursor()
	try:
		c.execute('''
		CREATE TABLE "Refund" (
		  "order_id" varchar(32),
		  "order_no" varchar(32),
		  "order_purchaser" varchar(32),
		  "order_date" DATE(32),
		  "order_price" varchar(100),
		  "order_type" varchar(32),
		  "train_passenger" varchar(32),
		  "train_date" DATE(32),
		  "train_no" varchar(32),
		  "train_price" varchar(32),
		  "transfer_fee" varchar(32),
		  "drawback_fee" varchar(32),
		  "train_type" varchar(32),
		  "start_station" varchar(32),
		  "start_lng" varchar(32),
		  "start_lat" varchar(32),
		  "stop_station" varchar(32),
		  "stop_lng" varchar(32),
		  "stop_lat" varchar(32),
		  "sit_type" varchar(32),
		  "sit_row" varchar(32),
		  "sit_no" varchar(32),
		  "sit_flow" varchar(32)
		);''')
		conn.commit()
		c.execute('''
		CREATE TABLE "change" (
		  "order_id" varchar(32),
		  "order_no" varchar(32),
		  "order_purchaser" varchar(32),
		  "order_date" DATE(32),
		  "order_count" varchar(32),
		  "order_price" varchar(32),
		  "order_type" varchar(32),
		  "train_passenger" varchar(32),
		  "train_date" DATE(32),
		  "train_no" varchar(32),
		  "train_price" varchar(32),
		  "train_type" varchar(32),
		  "start_station" varchar(32),
		  "start_lng" varchar(32),
		  "start_lat" varchar(32),
		  "stop_station" varchar(32),
		  "stop_lng" varchar(32),
		  "stop_lat" varchar(32),
		  "sit_type" varchar(32),
		  "sit_row" varchar(32),
		  "sit_no" varchar(32),
		  "sit_flow" varchar(32)
		);''')
		conn.commit()
		c.execute('''
		CREATE TABLE "etm_aio" (
		  "order_id" varchar(32),
		  "order_no" varchar(32),
		  "order_purchaser" varchar(32),
		  "order_date" DATE(32),
		  "order_count" varchar(32),
		  "order_price" varchar(32),
		  "order_type" varchar(32),
		  "train_passenger" varchar(32),
		  "train_date" DATE(32),
		  "train_no" varchar(32),
		  "train_price" varchar(32),
		  "drawback_fee" varchar(32),
		  "transfer_fee" varchar(32),
		  "train_type" varchar(32),
		  "start_station" varchar(32),
		  "start_lng" varchar(32),
		  "start_lat" varchar(32),
		  "stop_station" varchar(32),
		  "stop_lng" varchar(32),
		  "stop_lat" varchar(32),
		  "sit_type" varchar(32),
		  "sit_row" varchar(32),
		  "sit_no" varchar(32),
		  "sit_flow" varchar(32),
		  "ticket_entrance" varchar(32)
		);''')
		conn.commit()
		c.execute('''
		CREATE TABLE "purchase" (
		  "order_id" varchar(32),
		  "order_no" varchar(32),
		  "order_purchaser" varchar(32),
		  "order_date" DATE(32),
		  "order_count" varchar(32),
		  "order_price" varchar(32),
		  "order_type" varchar(32),
		  "train_passenger" varchar(32),
		  "train_date" DATE(32),
		  "train_no" varchar(32),
		  "train_price" varchar(32),
		  "drawback_fee" varchar(32),
		  "transfer_fee" varchar(32),
		  "train_type" varchar(32),
		  "start_station" varchar(32),
		  "start_lng" varchar(32),
		  "start_lat" varchar(32),
		  "stop_station" varchar(32),
		  "stop_lng" varchar(32),
		  "stop_lat" varchar(32),
		  "sit_type" varchar(32),
		  "sit_row" varchar(32),
		  "sit_no" varchar(32),
		  "sit_flow" varchar(32),
		  "ticket_entrance" varchar(32)
		);''')
		conn.commit()
		conn.close()
	except sqlite3.OperationalError:
		print ("database already exists")
