import sqlite3
conn =sqlite3.connect('www.db')
c=conn.cursor()

try:
	c.execute('''
	CREATE TABLE "Refund" (
	  "id" INTEGER(4) NOT NULL,
	  "order_no" INTEGER(32),
	  "order_purchaser" TEXT(32),
	  "order_date" DATE(32),
	  "order_price" NUMBER,
	  "order_type" TEXT(32),
	  "train_passenger" TEXT(32),
	  "train_date" DATE(32),
	  "train_no" INTEGER(32),
	  "train_price" NUMBER(32),
	  "Transfer_fee" TEXT,
	  "drawback_fee" TEXT,
	  "train_type" TEXT(32),
	  "start_station" TEXT(32),
	  "stop_station" TEXT(32),
	  "sit_type" TEXT(32),
	  "sit_row" TEXT(32),
	  "sit_no" INTEGER(32),
	  "sit_flow" TEXT(32),
	  PRIMARY KEY ("id")
	);
	CREATE TABLE "change" (
	  "id" INTEGER(4) NOT NULL,
	  "order_no" INTEGER(32),
	  "order_purchaser" TEXT(32),
	  "order_date" DATE(32),
	  "order_price" NUMBER,
	  "order_type" TEXT(32),
	  "train_passenger" TEXT(32),
	  "train_date" DATE(32),
	  "train_no" INTEGER(32),
	  "train_price" NUMBER(32),
	  "train_type" TEXT(32),
	  "start_station" TEXT(32),
	  "stop_station" TEXT(32),
	  "sit_type" TEXT(32),
	  "sit_row" TEXT(32),
	  "sit_no" INTEGER(32),
	  "sit_flow" TEXT(32),
	  PRIMARY KEY ("id")
	);
	CREATE TABLE "purchase" (
	  "id" INTEGER(4) NOT NULL,
	  "order_no" INTEGER(32),
	  "order_purchaser" TEXT(32),
	  "order_date" DATE(32),
	  "order_price" NUMBER,
	  "order_type" TEXT(32),
	  "train_passenger" TEXT(32),
	  "train_date" DATE(32),
	  "train_no" INTEGER(32),
	  "train_price" NUMBER(32),
	  "train_type" TEXT(32),
	  "start_station" TEXT(32),
	  "stop_station" TEXT(32),
	  "sit_type" TEXT(32),
	  "sit_row" TEXT(32),
	  "sit_no" INTEGER(32),
	  "sit_flow" TEXT(32),
	  PRIMARY KEY ("id")
	);''')
except sqlite3.OperationalError:
	print ("database already exists")


conn.commit()
conn.close