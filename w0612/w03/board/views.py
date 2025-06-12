from django.shortcuts import render, redirect
# ajax 전송에 필요한 선언
from django.http import HttpResponse, JsonResponse
from django.core import serializers     #json타입
from django.views.decorators.csrf import csrf_exempt    # csrf 토큰이 없을때 예외처리
from board.models import Board

# form 게시판 - GET, POST
def list(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
        context = {'list':qs}
        return render(request, 'board/list.html', context)
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        print('넘어온 데이터 : ', id, btitle, bcontent)
        
        # db 저장
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        
        return redirect('/board/list/')
    
def view(request):
    bno = request.GET.get('bno')
    print('넘어온 bno : ', bno)
    # 데이터 넘기기 : context, json
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'board/view.html', context)

# form - get, post
def list2(request):
    if request.method == 'GET':
        qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
        context = {'list':qs}
        return render(request, 'board/list2.html', context)
    elif request.method == 'POST':
        return render(request, 'board/list2.html')
    
def view2(request, bno):
    print('넘어온 bno : ', bno)
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'board/view2.html', context)


def list3(request):
    qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    context = {'list':qs}
    return render(request, 'board/list3.html', context)

# ajax3 - Board 모든 데이터 가져오기
def ajax3(request):
    qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    print('데이터 : ', qs)
    a = request.POST.get('sampleId')
    print('넘어온 데이터 : ', a)
    list_qs = serializers.serialize('json', qs)
    print('변경 타입 : ', list_qs)
    context = {'result':'성공', 'list':list_qs}
    return JsonResponse(context)


