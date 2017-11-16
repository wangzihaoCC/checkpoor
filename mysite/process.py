#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

import numpy as np
from numpy import newaxis

def process_rank(dblist,dim):
	arr0 = np.array(dblist)
	arr = np.delete(arr0,1,axis=1)
	arr[arr == None] = 0
	arr = arr.astype(np.float32)

	#复制一个出来
	arr2 = arr.copy()

	#给地域打分
	arr2[:,1]=np.where((arr2[:,1] == 2.)|(arr2[:,1] == 1),1,0)   #假设地区1. 和 2. 是贫困地区

	#给吃饭次数打分
	arr2[:,2]=np.where(arr2[:,2] > arr[:,2].mean(),1,0) #大于平均值

	#给吃饭金额打分
	arr2[:,3]=np.where(arr2[:,3] > arr[:,3].mean(),1,0) #大于平均值

	#给吃饭金额方差打分
	arr2[:,4]=np.where(arr2[:,4] < arr[:,4].mean(),1,0) #小于平均值

	#给成绩打分
	arr2[:,5]=np.where(arr2[:,5] > arr[:,5].mean(),1,0) #大于平均值

	#取出id
	idarr = arr2[:,0]
	arr2[:,0] = 0

	#假设后维度的权重总和为100分
	#x = np.array([0.,10.,30.,30.,20.,10.])
	x = np.array(dim).astype(np.float32)

	#计算
	arr3 = arr2 * x

	#最终成绩，需求学号(arr)、姓名、积分(mark)、排名(x)
	mark = np.sum(arr3,axis = 1)
	mark = mark[:,newaxis]
	#rankresult = np.vstack((arr[:,:2],mark)).T.astype(np.int64) #合并学号和成绩，
	rankresult = np.concatenate((arr0[:,:2],mark),axis=1) #合并学号\名字\成绩
	#rankresult = rankresult[np.lexsort(rankresult.T)] #对成绩进行排序
	rankresult = rankresult[np.lexsort(-rankresult[:,[0,2]].T)]
	#在最后一列加上顺序
	CRow = np.arange(1,rankresult.shape[0]+1)
	CRow = CRow[:,newaxis]
	rankresult = np.concatenate((rankresult,CRow),axis=1).tolist()
	return rankresult
