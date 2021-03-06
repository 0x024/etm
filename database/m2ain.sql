/*
 Navicat SQLite Data Transfer

 Source Server         : etm
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 30/08/2020 22:14:43
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Refund
-- ----------------------------
DROP TABLE IF EXISTS "Refund";
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
		);

-- ----------------------------
-- Table structure for change
-- ----------------------------
DROP TABLE IF EXISTS "change";
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
		);

-- ----------------------------
-- Table structure for etm_aio
-- ----------------------------
DROP TABLE IF EXISTS "etm_aio";
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
		);

-- ----------------------------
-- Table structure for location
-- ----------------------------
DROP TABLE IF EXISTS "location";
CREATE TABLE "location" (
  "station" TEXT(32),
  "formatted_address" TEXT(32),
  "country" TEXT(32),
  "province" TEXT(32),
  "city" TEXT(32),
  "citycode" TEXT(32),
  "district" TEXT(32),
  "street" TEXT(32),
  "streetnumber" INTEGER(32),
  "adcode" TEXT(32),
  "lng" TEXT(32),
  "lat" TEXT(32)
);

-- ----------------------------
-- Table structure for purchase
-- ----------------------------
DROP TABLE IF EXISTS "purchase";
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
		);

PRAGMA foreign_keys = true;
