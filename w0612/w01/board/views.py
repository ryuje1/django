from django.shortcuts import render, redirect
# ajax 전송에 필요한 선언
from django.http import HttpResponse, JsonResponse
from django.core import serializers     #json타입
from django.views.decorators.csrf import csrf_exempt    # csrf 토큰이 없을때 예외처리
from board.models import Board

# form 게시판 - GET, POST
def list(request):
    # db 데이터 모두 가져오기
    qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    context = {'list':qs}   # html 전달
    return render(request, 'board/list.html', context)