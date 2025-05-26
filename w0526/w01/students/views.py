from django.shortcuts import render
from students.models import Students

def list(request):
    return render(request, 'list.html')

def write(request):
    return render(request, 'write.html')

def update(request):
    return render(request, 'update.html')

def delete(request):
    return render(request, 'delete.html')