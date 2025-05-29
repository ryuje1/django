from django.shortcuts import render

def list(request):
    return render(request, 'board/notice_list.html')

def read(request):
    return render(request, 'board/notice_read.html')

def write(request):
    return render(request, 'board/write.html')
