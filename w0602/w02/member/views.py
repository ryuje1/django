from django.shortcuts import render
from member.models import Member

def login(request):
    if request.method == 'GET':
        # 쿠키 세션
        return render(request, 'member/login.html')
    
    elif request.method == 'POST':
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        
        try:
            qs = Member.objects.get(id=id, pw=pw)
        except:
            # id, pw 같은 게 없을때
            context = {'msg':0}
            return render(request, 'member/login.html', context)
        
        context = {'msg':1}
        return render(request, 'member/login.html', context)