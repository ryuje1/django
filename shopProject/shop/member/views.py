from django.shortcuts import render, redirect
from django.http import JsonResponse
from member.models import Member
import random
import numpy as np

# get : 로그인페이지, post : 로그인 확인
def login(request):
    ## 쿠키 정보 가져오기
    cook_id = request.COOKIES.get('cook_id', '')
    context = {'cook_id':cook_id}
    
    if request.method == 'GET':
        return render(request, 'member/login.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        idsave = request.POST.get('idsave')
        print('넘어온 id, pw, idsave : ', id, pw, idsave)
        
        ## db확인
        qs = Member.objects.filter(id=id, pw=pw)    # 없으면 None
        print(qs)
        if qs:
            msg = 1
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
        else:
            msg = 0
        
        context['msg'] = msg
        response = render(request, 'member/login.html', context)
        if idsave:
            response.set_cookie('cook_id', id, max_age=60*60*24)    # 하루동안 저장
        else:
            response.delete_cookie('cook_id')
        return response

# 로그아웃
def logout(request):
    ### 세션 모두 삭제
    request.session.clear()
    msg = 2
    context = {'msg':msg}
    return render(request, 'member/login.html', context)

def step01(request):
    return render(request, 'member/step01.html')

def emailSend(request):
    email = request.POST.get('email')
    txt = 'abcdefghijklmnopqrstuvwsyz0123456789'
    rno = random.randrange(0, 35, 10)
    context = {'msg':'success'}
    return JsonResponse(context)