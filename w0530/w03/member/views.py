from django.shortcuts import render
from member.models import Member

def login(request):
    # 쿠키 읽어오기
    cookie_info = request.COOKIES
    cookie_id = request.COOKIES.get('cookie_val', '')       # 있으면 aaa, 없으면 None 읽어옴 / None일때 ' ' 공백처리
    print('cookie_id :', cookie_id)
    context = {'cookie_info':cookie_info, 'cookie_id':cookie_id}
    
    if request.method == 'GET':     # 로그인 페이지 열기
        return render(request, 'member/login.html', context)
    
    # 아이디 저장 체크박스
    elif request.method == 'POST':  # id, pw 확인
        id = request.POST.get('id')
        pw = request.POST.get('pw')
        cookie_val = request.POST.get('cookie_val')
        
        # id, pw 확인 - 없으면 error 예외처리 필요
        try:
            qs = Member.objects.get(id=id, pw=pw)
            # session 추가
            request.session['session_id'] = qs.id       # session_id = key 값
            request.session['session_nickName'] = qs.nickName
            msg = 1     # id, pw가 있음
            print("데이터 여부 : 존재")
        except:
            msg = 0     # id, pw가 없음
            print("데이터 여부 : 없음")
        context = {'msg':msg, 'cookie_info':cookie_info, 'cookie_id':cookie_id}
            
        context = {'msg':msg}
        response = render(request, 'member/login.html', context)
        # response 쿠키 저장 (유저 : cookie 저장, server : session 저장)
        if cookie_val is not None:
            # cookie_val = 'id save'
            # max_age : 저장 시간 (60초*60분*24시간*365일 = 1년)
            response.set_cookie('cookie_id', id, max_age=60*60*24*365)    # cookie_id = key값 임의로 저장
        else:
            response.delete_cookie('cookie_val')
            
        return response
    
def logout(request):
    request.session.clear()
    context = {'msg':-1}
    return render(request, 'member/login.html', context)
