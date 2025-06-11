from django.shortcuts import render
# ajax 전송에 필요한 선언
from django.http import HttpResponse, JsonResponse
from django.core import serializers     #json타입
from django.views.decorators.csrf import csrf_exempt    # csrf 토큰이 없을때 예외처리

def list(request):
    return render(request, 'board/list.html')

# form 데이터 전송 - get, post
def view(request):
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    
    context = {'id':id, 'name':name}
    return render(request, 'board/view.html', context)

# ajax 데이터 전송 - get, post
def view2(request):
    # html에서 데이터 전달
    id = request.POST.get('id', '')
    name = request.POST.get('name', '')
    # QuerySet, QueryList -> list타입으로 변경 필요
    # models db 데이터가 있으면 list 타입으로 변경 후 전송해야 함
    
    # 데이터를 html로 전송
    context = {'id':id, 'name':name, 'result':'success', 'pw':'1111'}
    
    return JsonResponse(context)