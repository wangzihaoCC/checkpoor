#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import pymysql
import numpy as np
import logging
 

#读mysql
def readdb(sql):
	conn = pymysql.Connect(host="localhost",port=3306,user="jeffrey",passwd="123456Xx!",db="TESTDB",charset="utf8")
	cursor = conn.cursor()
	try:
		sat = cursor.execute(sql)
		conn.commit()
		results = cursor.fetchall()	
		return results
	except:
		conn.rollback()
		print("sql error")
	finally:
	    conn.close();


def createview(sql):
	conn = pymysql.Connect("localhost","jeffrey","123456Xx!","TESTDB")
	cursor = conn.cursor()
	try:
		sat = cursor.execute(sql)
		conn.commit()
	except:
		conn.rollback()
		print("sql error")
	finally:
	    conn.close();







