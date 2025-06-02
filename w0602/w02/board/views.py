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
        id = 'aaa'
        btitle = request.POST.get('btitle')
        bcontent = request.POST.get('bcontent')
        bfile = request.POST.get('bfile')
        
        qs = Board.objects.create(id=id, btitle=btitle, bcontent=bcontent)
        qs.bgroup = qs.bno
        qs.save()

        # return render(request, 'board/write.html')
        return redirect('board:list')