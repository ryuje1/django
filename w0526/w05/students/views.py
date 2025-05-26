from django.shortcuts import render
from students.models import Student

def list(request):
    qs = Student.objects.all()
    context = {"list":qs}
    return render(request, 'students/list.html', context)   # 변수 전달