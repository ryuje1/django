from django.shortcuts import render

def list(request):
    return render(request, 'list.html')

def view(request):
    return render(request, 'view.html')