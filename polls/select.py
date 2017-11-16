# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request):
    return render_to_response('index.html')
 
# 接收请求数据
def search(request):  
    request.encoding='utf-8'
    if 'starttime' in request.GET:
        starttime = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '无起始时间'
    if 'endtime' in request.GET:
        endtime = '你搜索的内容为: ' + request.GET['q']
    else:
        message = '无借书时间'  

    if(starttime & endtime):
    	message = str(starttime) + str(endtime)

    return HttpResponse(message)