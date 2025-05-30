from django.shortcuts import render, redirect
from member.models import Member

def login(request):
    # GET
    if request.method == 'GET':
        return render(request, 'member/login.html')
    # POST
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        try:
            qs = Member.objects.get(id=id)
            if qs.pw == pw:
                request.session['session_id'] = id
                txt = 1     # 로그인 성공
            else:
                txt = -1    # 아이디는 맞는데 패스워드 틀림
        except:
            txt = 0         # 아이디가 없음
        
        
        context = {'msg':txt}
        return render(request, 'member/login.html', context)

def logout(request):
    request.session.clear()
    context = {'msg':2}
    return render(request, 'member/login.html', context)
