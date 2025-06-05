from django.shortcuts import render, redirect
from board.models import Board

def list(request):
    qs = Board.objects.all().order_by('-bno')
    context = {'list':qs}
    return render(request, 'board/list.html', context)


def write(request):
    if request.method == 'GET':
        return render(request, 'board/write.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.FILES.get('bfile')
        print('데이터 : ', id, btitle, bcontent, bfile)
        
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent, bfile=bfile)
        qs.bgroup = qs.bno
        qs.save()
        
        context = {'msg':1}
        return render(request, 'board/write.html', context)


def view(request, bno):
    qs = Board.objects.get(bno=bno)
    context = {'board':qs}
    return render(request, 'board/view.html', context)


def update(request, bno):
    if request.method == 'GET':
        qs = Board.objects.get(bno=bno)
        context = {'board':qs}
        return render(request, 'board/update.html', context)
    
    elif request.method == 'POST':
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile_pre = request.POST.get('bfile_pre','')
        bfile = request.FILES.get('bfile','')
        if not bfile:
            bfile = bfile_pre
        
        qs = Board.objects.get(bno=bno)
        qs.btitle = btitle
        qs.bcontent = bcontent
        qs.bfile = bfile
        qs.save()
        
        context = {'msg':1, 'board':qs}
        return render(request, 'board/update.html', context)
    
def delete(request, bno):
    Board.objects.get(bno=bno).delete()
    
    return redirect('/board/list/')