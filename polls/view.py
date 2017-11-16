from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render

# 接收请求数据,筛选权重设置
def reachget(request):
    request.encoding='utf-8'
    context = {}
    context['ex1'] = request.GET['ex1']
    context['ex2'] = request.GET['ex2']
    context['ex3'] = request.GET['ex3']
    context['ex4'] = request.GET['ex4']
    context['ex5'] = request.GET['ex5']
    return render(request, 'list.html', context)