from django.shortcuts import render

def list(request):
    return render(request, 'kakaomap/list.html')

def list2(request):
    return render(request, 'kakaomap/list2.html')