from django.shortcuts import render

def list(request):
    return render(request, 'board/list.html')

def view(request):
    return render(request, 'board/view.html')

def write(request):
    return render(request, 'board/write.html')
