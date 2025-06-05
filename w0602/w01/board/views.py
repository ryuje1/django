from django.shortcuts import render, redirect
from board.models import Board
from django.core.paginator import Paginator
from django.db.models import F, Q

# 게시판 리스트
def list(request):
    search = request.GET.get('search', '')
    category = request.GET.get('category', '')
    page = int(request.GET.get('page', 1))  # 현재 페이지 가져오기
    print('검색 데이터 :', search, category)
    
    if search == '':
        # 모든 데이터 가져오기
        qs = Board.objects.order_by('-bgroup', 'bstep')
        # 페이지 처리
        paginator = Paginator(qs, 10)    # 페이지 처리 (100개 게시글을 10개씩 나눔)
        list = paginator.get_page(page) # 해당 페이지 가져오기 (10개 중 해당하는 게시글 가져옴)
        context = {'list':list, 'page':page}
        return render(request, 'board/list.html', context)
    else:
        # 검색된 데이터 가져오기
        qs = Board.objects.filter(Q(btitle__contains=search) | Q(bcontent__contains=search)).order_by('-bgroup', 'bstep')
        # 페이지 처리
        paginator = Paginator(qs, 10)    # 페이지 처리 (100개 게시글을 10개씩 나눔)
        list = paginator.get_page(page) # 해당 페이지 가져오기 (10개 중 해당하는 게시글 가져옴)
        context = {'list':list, 'page':page, 'category':category, 'search':search}
        return render(request, 'board/list.html', context)

# 게시판 글쓰기 페이지, 쓰기 저장
def write(request):
    if request.method == 'GET':     # 글쓰기 페이지
        return render(request, 'board/write.html')
    elif request.method == 'POST':  # 글쓰기 저장
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        # DB 저장 후 qs 변수로 다시 리턴받음
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()
        
        print('데이터 확인 :', btitle, bcontent, bfile)
        print('데이터 추가 :', qs.bgroup, qs.bstep, bfile)
        
        return redirect('board:list')

# 게시판 상세보기
def view(request, bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'board/view.html', context)

# 글 수정 페이지, 수정저장
def update(request, bno):
    if request.method == 'GET':         # 글 수정 페이지
        qs = Board.objects.get(bno=bno) # 1개 게시글 가져오기
        context = {'board':qs}
        return render(request, 'board/update.html', context)
    elif request.method == 'POST':      # 글 수정저장
        # 변경된 게시글을 가져오기 - 몇번 게시글인지 확인
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
                
        # 변경된 게시글 저장
        # 변경할 게시글 가져온 후 변경된 내용 저장
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.save()
        
        context = {'msg':1}     # 글 수정 저장성공
        return render(request, 'board/update.html', context)