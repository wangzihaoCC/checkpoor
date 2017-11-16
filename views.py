# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render


def index(request):
    context          = {}
    context['aa'] = 'this is aa!'
    context['bb'] = 'this is bb!'
    context['amount'] = [17,18,24,22,7,20,23,17,16,15,29]
    context['calendar'] = str(["2017-10-10","2017-10-11","2017-10-12","2017-10-13"]).encode("utf-8")
    context['data']= [17,18,24,22]
    return render(request, 'index.html', context)

def reachget(request):  
    request.encoding='utf-8'
    context = {}
    context['starttime'] = request.GET['starttime']
    context['endtime'] = request.GET['endtime']
    return render(request, 'list.html', context)