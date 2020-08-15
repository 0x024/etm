/*
 Navicat Premium Data Transfer

 Source Server         : etm
 Source Server Type    : SQLite
 Source Server Version : 3030001
 Source Schema         : main

 Target Server Type    : SQLite
 Target Server Version : 3030001
 File Encoding         : 65001

 Date: 13/08/2020 23:47:13
*/

PRAGMA foreign_keys = false;

-- ----------------------------
-- Table structure for etm
-- ----------------------------
DROP TABLE IF EXISTS "etm";
CREATE TABLE "etm" (
  "id" INTEGER(4) NOT NULL,
  "purchaser" TEXT(32),
  "order_no" INTEGER(32),
  "order_date" DATE(32),
  "order_type" TEXT(32),
  "passenger" TEXT(32),
  "train_date" DATE(32),
  "start_station" TEXT(32),
  "stop_station" TEXT(32),
  "train_no" INTEGER(32),
  "train_price" NUMBER(32),
  "train_type" TEXT(32),
  "sit_type" TEXT(32),
  "sit_row" TEXT(32),
  "sit_no" INTEGER(32),
  "ticket_entrance" TEXT(32),
  "Transfer_fee" TEXT(32),
  PRIMARY KEY ("id")
);

PRAGMA foreign_keys = true;
