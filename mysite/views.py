# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from . import getlist,process



def index(request):
	request.encoding='utf-8'
	context = {}
	context['aa'] = 'this is aa!'
	context['bb'] = 'this is bb!'
	context['amount'] = [17,18,24,22,7,20,23,17,16,15,29]
	context['calendar'] = str(["2017-10-10","2017-10-11","2017-10-12","2017-10-13"]).encode("utf-8")
	context['data']= [17,18,24,22]
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





