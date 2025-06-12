from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers #json타입
from django.views.decorators.csrf import csrf_exempt #csrf토큰이 없을때 예외처리
from board.models import Board

# bwrite 글쓰기 - ajax 
# 1. 데이터 전송 유무, 2. db저장, 3. json타입 변환, 4. 전송
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    print('html에서 server측으로 전달 데이터 : ', id, btitle, bcontent)
    
    # db저장
    qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    # json 데이터 변환(serial)
    
    
    context = {'result':'success'}
    return JsonResponse(context)