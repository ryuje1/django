from django.shortcuts import render, redirect
from students.models import Student

def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'students/list.html', context)

def write(request):
    return render(request, 'students/write.html')

def writeOK(request):
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    
    Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby).save()
    
    return redirect('/students/list/')

def view(request, no):
    qs = Student.objects.get(no=no)
    context = {'stu':qs}
    return render(request, 'students/view.html', context)
