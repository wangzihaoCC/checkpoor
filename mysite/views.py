# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from . import getlist,process
import json

#用在首页中查消费那个chart
t = "limit 100"
sqlAmount = '''select amount from messorder %s;''' %(t)
sqlday = '''select date_format(ordertime,'%Y-%m-%d %H') as dt,count(orderid) as cid from messorder where ordertime >= date_sub(now(), INTERVAL 1 DAY) AND ordertime <= now() group by dt;'''
sqlweek = '''select date_format(ordertime,'%Y-%m-%d') as dt,count(orderid) as cid from messorder where ordertime >= date_sub(now(), INTERVAL 7 DAY) AND ordertime <= now()  group by dt;'''
sqlmonth = '''select date_format(ordertime,'%Y-%m-%d') as dt,count(orderid) as cid from messorder where ordertime >= date_sub(now(), INTERVAL 90 DAY) AND ordertime <= now()  group by dt;'''

def Getchart2(sql):
	chart2Data = list(getlist.readdb(sqlmonth))
	TimeList =[]
	DateList = []
	for i in chart2Data:
		TimeList.append(i[0])
		DateList.append(i[1])
		
	Getchart2Data = [TimeList,DateList]
	return Getchart2Data

def index(request):
	request.encoding='utf-8'
	chartData = list(getlist.readdb(sqlAmount))
	AmountList =[]
	for (i,) in chartData:
		AmountList.append(i)
	context = {}
	context['amount'] = AmountList
	context['amountlength'] = len(AmountList)

	Getchart2Data = Getchart2(sqlmonth)

	
	context['calendar'] = str(Getchart2Data[0]).encode("utf-8")
	context['data']= Getchart2Data[1]
	return render(request, 'index.html', context)




sql1 = '''select stuid,stuname,local,ordertime,avgorder,std,avgmark from maintable;'''





def reachget(request):  
    request.encoding='utf-8'
    dim1,dim2,dim3,dim4,dim5,t1,t2 = request.GET['ex1'],request.GET['ex2'],request.GET['ex3'],request.GET['ex4'],request.GET['ex5'],request.GET['starttime'],request.GET['endtime']

    context = {}
    context['dim1'] = dim1
    context['dim2'] = dim2
    context['dim3'] = dim3
    context['dim4'] = dim4
    context['dim5'] = dim5
    context['t1'] = t1
    context['t2'] = t2
    dim = [0,dim1,dim2,dim3,dim4,dim5]
    #创建视图

    createviewSQL = '''
	DROP VIEW IF exists maintable;
	DROP VIEW IF exists tempmessorder;
	CREATE view tempmessorder as
	select * from messorder
	where ordertime between %s and %s; 
	CREATE view maintable as
	select student.stuid , 
	student.stuname , 
	student.local , 
	count(tempmessorder.orderid) div 3 as ordertime,
	format(avg(tempmessorder.amount),2) as avgorder,
	format(std(tempmessorder.amount),2) as std,
	format(avg(mark.mark),2) as avgmark
	from tempmessorder right join student on tempmessorder.userid = student.stuid left join mark on student.stuid = mark.userid
	group by student.stuid;
	''' % (t1,t2)

    getlist.createview(createviewSQL)

    #查询视图
    dbresult = list(getlist.readdb(sql1)) 

    #加工排序
    processresult = process.process_rank(dbresult,dim)
    context['processresult'] = processresult

    return render(request, 'list.html', context)





