from django.shortcuts import render

def index(request):
    cook_info = request.COOKIES         # 모든 쿠키 정보 가져오기
    test_id = request.COOKIES.get('test', '')   # 쿠키 정보 1개 읽기
    print("쿠키 정보 :", cook_info)
    context = {'cook_info':cook_info}
    response = render(request, 'index.html', context)
    if test_id == '':
        response.set_cookie('test', 'aaa')  # 쿠키 1개 저장
        print('test 쿠키 저장')
    else:
        response.delete_cookie('test')      # 쿠키 삭제
        print('test 쿠키 삭제')
    return response