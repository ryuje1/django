from django.shortcuts import render, redirect
from students.models import Student

# 학생정보리스트
def list(request):
    qs = Student.objects.all()
    context = {'list':qs}
    # 폴더 앞에 / 안붙임
    return render(request, 'students/list.html', context)

# 학생 정보 저장
def writeOK(request):
    # 학생 정보 저장
    name = request.POST.get('name')
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    # 취미 - 체크박스 (리스트로 넘어옴)
    hobby = request.POST.getlist('hobby')
    # list 타입 -> str 타입으로 변경
    hobby = ','.join(hobby) # 'game,golf,swim'
    print('저장정보 hobby :', hobby)    # ['game','golf','swim']
    
    Student(name=name, major=major, grade=grade, age=age, gender=gender, hobby=hobby, memo='등록합니다.').save()


    return redirect('/students/list/')

# 학생 정보 등록페이지 열기
def write(request):
    return render(request, 'students/write.html')

# # 학생 정보 등록페이지 오픈
# def write(request):
#     if request.method == 'GET':
#         return render(request, 'students/write.html')
#     else : # if request.method == 'POST':
#         return redirect('/students/list/')


# 학생 정보 상세보기
def view(request, no):
    try:
        qs = Student.objects.get(no=no)
    except:
        qs = None
    print('전달 no :', no)
    context = {'stu':qs}
    return render(request, 'students/view.html', context)
    

# 학생 정보 수정 페이지 열기
def update(request, no):
    qs = Student.objects.get(no=no) # set 타입 1개 - 없어도 에러 안남
    context = {'stu':qs}
    # qs = Student.filter(no=no)      # 리스트 타입 - 없으면 에러남
    return render(request, 'students/update.html', context)

# 학생 정보 수정 완료
def updateOK(request):
    no = request.POST.get('no')
    qs = Student.objects.get(no=no)
    # 데이터 수정
    qs.name = request.POST.get('name')
    qs.major = request.POST.get('major')
    qs.grade = request.POST.get('grade')
    qs.age = request.POST.get('age')
    qs.gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')
    hobby = ','.join(hobby)
    qs.hobby = hobby
    qs.save()

    return redirect(f'/students/view/{no}/')

def delete(request, no):
    qs = Student.objects.get(no=no).delete()
    # return redirect('/students/list/')
    return redirect('students:list')        # app_name:path name