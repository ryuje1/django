from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from students.models import Student

# 학생정보 읽어오기
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    return render(request, 'students/list.html', context)

# 학생정보 상세보기
def view(request):
    name = request.GET.get('name')
    qs = Student.objects.get(name=name)
    context = {'s_view':qs}
    return render(request, 'students/view.html', context)

# 학생정보 등록
def write(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        Student(name=name, major=major, grade=grade, age=age, gender=gender).save()
        return redirect('/students/list/')
    else:
        return render(request, 'students/write.html')

# 학생정보 수정
def update(request, name):
    if request.method == 'GET':
        qs = Student.objects.get(name=name)
        context = {'s_view':qs}
        return render(request, 'students/update.html', context)
    else:
        name2 = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        
        qs = Student.objects.get(name=name)
        qs.name = name2
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        qs.save()
        return redirect('/students/list/')
    
# 학생정보 삭제
def delete(request, name):
    qs = Student.objects.get(name=name)
    qs.delete()
    return redirect('/students/list/')