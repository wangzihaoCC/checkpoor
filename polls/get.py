#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import pymysql

#读mysql
def readdb(sql):
	conn = pymysql.Connect("localhost","jeffrey","123456Xx!","TESTDB")
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

sql1 = '''select stuid,local,ordertime,avgorder,std,avgmark from maintable;'''


result = list(readdb(sql1))
arr = np.array(result)
arr[arr == None] = 0
arr = arr.astype(np.float32)

#复制一个出来
arr2 = arr.copy()

#给地域打分
arr2[:,1]=np.where((arr2[:,1] == 2.)|(arr2[:,1] == 1),1,0)   #假设地区1. 和 2. 是贫困地区

#给吃饭次数打分
arr2[:,2]=np.where(arr2[:,2] > arr[:,2].mean(),1,0)

#给吃饭金额打分
arr2[:,3]=np.where(arr2[:,3] > arr[:,3].mean(),1,0)

#给吃饭金额方差打分
arr2[:,4]=np.where(arr2[:,4] > arr[:,4].mean(),1,0)

#给成绩打分
arr2[:,5]=np.where(arr2[:,5] > arr[:,5].mean(),1,0)

#取出id
idarr = arr2[:,0]
arr2[:,0] = 0

#假设后维度的权重总和为100分
x = np.array([0.,10.,30.,30.,20.,10.])

#计算
arr3 = arr2 * x

#最终成绩
mark = np.sum(arr3,axis = 1)

Rank = np.vstack((arr[:,0],mark)).tolist()
print(Rank)



