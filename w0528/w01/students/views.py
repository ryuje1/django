from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from students.models import Student     # Student 테이블 불러오기

# 학생 정보 리스트
def list(request):
    # DB검색 = objects.all() : 전체 가져오기, objects.get() : 해당되는 것 가져오기
    # objects.filter() : 검색 기능 (QuerySet으로 넘어옴) - __contains, gte, gt, lte, lt
    # objects.order_by() : 정렬, -역순정렬
    # qs = Student.objects.all()      # 전체 가져오기
    # qs = Student.objects.order_by('id')      # 순차정렬
    qs = Student.objects.order_by('-id')      # 역순정렬
    context = {'list':qs, 'count':100, 'id':'aaa'}   # 딕셔너리 타입으로 전달
    return render(request, 'students/list.html', context)
    

# 학생 정보 등록
def write(request):
    if request.method == 'POST':  # POST 방식으로 들어올때 - 정보를 DB에 저장
        name = request.POST.get('name')
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print('입력된 정보 :', name, major, grade, age, gender)
        ## DB 저장
        ## 1. 데이터.save(), Student.objects.create(데이터)
        Student(name=name, major=major, grade=grade, age=age, gender=gender).save()
        print("student 객체 저장")
        return redirect('/students/list/')
    
    else:   # GET 방식으로 들어올때
        print("request method :", request.method)
        return render(request, 'students/write.html')
    
    
# 학생 정보 상세보기
def view(request):
    name = request.GET.get('name')
    print('전달 이름 :', name)
    qs = Student.objects.get(name=name)
    context = {'stu':qs}
    return render(request, 'students/view.html', context)


# 학생 정보 수정
# GET - view와 동일 / POST - write와 동일
def update(request, name):
    if request.method == "GET":
        print("학생이름 :", name)
        qs = Student.objects.get(name=name)
        context = {'stu':qs}
        return render(request, 'students/update.html', context)
    else:
        # name = request.POST.get('name')  # 이름은 primary key라 수정 불가
        name2 = request.POST.get('name')   # 이름 수정 가능
        major = request.POST.get('major')
        grade = request.POST.get('grade')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        print('입력된 정보 :', name, major, grade, age, gender)
        ## DB 수정
        # 1. 회원 검색
        qs = Student.objects.get(name=name)     # 해당되는 학생 정보 검색
        # 2. 회원정보 수정
        # qs.name = name    # 이름은 primary key라 수정 불가
        qs.name = name2   # 이름 수정 가능
        qs.major = major
        qs.grade = grade
        qs.age = age
        qs.gender = gender
        ## 3. 저장
        qs.save()
        print("student 객체 수정")
        return redirect('/students/list/')
    
# 학생 정보 삭제
def delete(request, name):
    print("삭제 이름 :", name)
    qs = Student.objects.get(name=name)     # 해당되는 학생 정보 검색
    qs.delete()     # 삭제
    return redirect('/students/list/')