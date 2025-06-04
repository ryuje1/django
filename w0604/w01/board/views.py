from django.shortcuts import render, redirect
from board.models import Board
from django.db.models import F

# 게시판 리스트
def list(request):
    qs = Board.objects.all().order_by('-bgroup', 'bstep')   # 1차 정렬 - bgroup 역순 / 2차 정렬 - bstep (bgroup 같은 게 있을 경우에만 정렬)
    context = {'list':qs}
    return render(request, 'board/list.html', context)

# 게시글 보기
def view(request, bno):
    # 조회수 변경
    # 1. qs값 수정
    # qs = Board.objects.get(bno=bno)
    # qs.bhit += 1
    # qs.save()
    
    # 2. F함수 사용 - filter 검색 후, qs에서 특정 컬럼의 값을 가져오는 함수
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit = F('bhit')+1)   # save까지 됨
    
    context = {'board':qs[0]}
    return render(request, 'board/view.html', context)

# 게시글 쓰기 - 게시글 페이지 열기, 게시글 저장
def write(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')
    elif request.method == 'POST':
        # 데이터 가져오기
        # id = request.session.session_id   # 세션에서 가져옴
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        print('가져온 데이터 :', id, btitle, bcontent, bfile)
        
        # 게시글 저장
        # 1. save() 방식
        # Board(id=id, btitle=btitle, bcontent=bcontent, bfile=bfile).save()      # bno를 가져올 수 없음
        
        # 2. create 방식
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bfile=bfile)
        qs.bgroup = qs.bno      # 수정할때 필요
        qs.save()
        
        context = {'msg':1}
        
        return render(request, 'board/write.html', context)

# 게시글 수정 - 수정 페이지 열기, 수정 저장
def update(request, bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request, 'board/update.html', context)
    
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        # qs.bfile = bfile
        qs.save()
        
        context = {'msg':1, 'board':qs}
        return render(request, 'board/update.html', context)

# 게시글 삭제
def delete(request, bno):
    ## 게시글 삭제
    Board.objects.get(bno=bno).delete()
    
    return redirect('/board/list/')

# 답글달기 - 답글달기 페이지 열기, 답글 저장
def reply(request, bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request, 'board/reply.html', context)
    
    elif request.method == 'POST':
        id = request.POST.get('id')     # session_id 가져옴
        bgroup = request.POST.get('bgroup')         # 부모의 bgroup
        bstep = int(request.POST.get('bstep'))      # 부모의 bstep
        bindent = int(request.POST.get('bindent'))  # 부모의 bindent
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        ## 답글달기 저장
        # 1. gt, lt, gte, lte 언더바 2개 넣어야함
        # 부모보다 bstep 더 큰 것(필터링으로 찾기), 모든 자식들은 전부 bstep을 1씩 증가시켜야 함
        # F함수 : 현재 찾아진 컬럼의 값을 모두 가져옴
        reply_qs = Board.objects.filter(bgroup=bgroup, bstep__gt=bstep)
        reply_qs.update(bstep = F('bstep')+1)
        # 2. db저장
        qs = Board.objects.create(id=id, bgroup=bgroup, bstep=bstep+1, bindent=bindent+1, btitle=btitle, bcontent=bcontent, bfile=bfile)
        
        context = {"msg":1, "board":qs}
        return render(request, 'board/reply.html', context)