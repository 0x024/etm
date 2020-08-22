/*
 Navicat Premium Data Transfer

 Source Server         : etm
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 19/08/2020 23:47:57
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for Refund
-- ----------------------------
DROP TABLE IF EXISTS "Refund";
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

-- ----------------------------
-- Table structure for change
-- ----------------------------
DROP TABLE IF EXISTS "change";
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

-- ----------------------------
-- Table structure for purchase
-- ----------------------------
DROP TABLE IF EXISTS "purchase";
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
);

PRAGMA foreign_keys = true;
