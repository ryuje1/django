from django.shortcuts import render

def member(request):
    return render(request, 'member.html')