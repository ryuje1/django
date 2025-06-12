from django.shortcuts import render
from django.http import JsonResponse
from board.models import Board

# form 게시판 - get, post
def blist(request):
    ### db게시글 전체 가져오기
    qs = Board.objects.all().order_by('-ntchk', '-bgroup', 'bstep')
    ### json 타입으로 변경 (querySet 타입은 없기때문에 리스트로 변경)
    l_qs = list(qs.values())
    print('리스트 타입 : ', l_qs)
    context = {'result':'success', 'list':l_qs}
    return JsonResponse(context)

# 게시글 등록
def bwrite(request):
    id = request.POST.get('id')
    btitle = request.POST.get('btitle')
    bcontent = request.POST.get('bcontent')
    
    # db 저장
    qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    
    #json 타입 변환
    l_qs = list(Board.objects.filter(bno=qs.bno).values())
    
    context = {'result':'성공', 'board':l_qs}
    return JsonResponse(context)

# 게시글 삭제
def bdelete(request):
    ## db삭제
    bno = request.POST.get('bno')
    qs = Board.objects.get(bno=bno)
    context = {'result':'success'}
    return JsonResponse(context)