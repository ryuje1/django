from django.shortcuts import render
from django.http import HttpResponse

def list(request):
    ### templates 폴더 안에 list.html 파일 존재
    return render(request, 'list.html')
    # return HttpResponse('리스트 페이지 연결')

def view(request):
    return render(request, 'view.html')

def write(request):
    return render(request, 'write.html')

def delete(request):
    return render(request, 'delete.html')