from django.shortcuts import render, redirect
from board.models import Board
# F : 검색된 필드에서 특정 컬럼의 값을 가져올때 사용
# Q : and(&), or(|), not(~) 연산을 사용할때 사용
from django.db.models import F, Q
from django.core.paginator import Paginator

# 게시판 리스트 - 일반 게시판리스트, 검색게시판리스트
def list(request):
    # 현재 페이지 int 변경
    page = int(request.GET.get('page', 1))      # 없을때 1페이지 넘겨줌 (default : None)
    
    # search 로 넘어올때
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')
    print('검색데이터 : ', category, search)
    
    
    if search == '':    # 일반리스트 - 검색으로 페이지가 넘어오지 않은 경우
        # 게시글 전체 가져오기
        qs = Board.objects.all().order_by('-bgroup', 'bstep')   # 1차 정렬 - bgroup 역순 / 2차 정렬 - bstep (bgroup 같은 게 있을 경우에만 정렬)
        # 페이지 분기
        paginator = Paginator(qs, 20)   # 100개 -> 10개씩 쪼개서 전달
        list = paginator.get_page(page) # 현재 페이지에 해당되는 게시글 전달
        context = {'list':list, 'page':page}
        return render(request, 'board/list.html', context)
    
    else:               # 검색리스트 - 검색으로 넘어온 경우
        # 게시글 전체 가져오기
        if category == 'all':
            qs = Board.objects.filter(Q(btitle__contains=search) | Q(bcontent__contains=search))
        elif category == 'btitle':
            qs = Board.objects.filter(btitle__contains=search)
        else:
            qs = Board.objects.filter(bcontent__contains=search)
        # 페이지 분기
        paginator = Paginator(qs, 20)   # 100개 -> 10개씩 쪼개서 전달
        list = paginator.get_page(page) # 현재 페이지에 해당되는 게시글 전달
        context = {'list':list, 'page':page, 'search':search, 'category':category}
        return render(request, 'board/list.html', context)
        

# 게시글 보기
def view(request, bno):
    # 조회수 변경
    # 1. qs값 수정
    # qs = Board.objects.get(bno=bno)
    # qs.bhit += 1
    # qs.save()
    
    # 2. F함수 사용 - filter 검색 후, qs에서 특정 컬럼의 값을 가져오는 함수
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    
    qs = Board.objects.filter(bno=bno)
    qs.update(bhit = F('bhit')+1)   # save까지 됨
    
    context = {'board':qs[0], 'category':category, 'search':search}
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
        bfile = request.FILES.get('bfile', '')
        print('파일 부분 : ', request.FILES)
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
        bfile_pre = request.POST.get('bfile_pre','')
        bfile = request.FILES.get('bfile','')       # 파일업로드
        if not bfile:   # 수정할때 파일 따로 첨부 안했으면 이전 파일을 집어넣는다는 의미. (안하면 이전 파일을 날리게됨)
            bfile = bfile_pre
        
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.bfile = bfile
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
        bfile = request.FILES.get('bfile', '')
        
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