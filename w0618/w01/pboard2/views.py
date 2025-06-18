from django.shortcuts import render
import requests
import json

## 전역변수
dlist = []  # list함수에서 공공데이터를 가지고 와서 view함수에 전달

# 공공데이터 리스트
def list(request):
    global dlist    # 전역변수 사용
    # 공공데이터 가져오기에 필요한 정보
    pageNo = 1
    serviceKey = 'bL05ehIVxrekLZkNPfKKTOw%2FG6cS1dFlgNuQS5K5hlHUuHGQn3MZAJ7GxH0IbYTxX4D5FPl6XzogD7CBxyrJyg%3D%3D'
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={serviceKey}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    
    # 공공데이터 가져오기
    response = requests.get(url)              # 공공데이터 가져온 타입 : str타입
    json_data = json.loads(response.text)     # json 타입으로 변경 - dict타입과 동일
    dlist = json_data['response']['body']['items']['item']
    print('10개 : ', dlist)
    context = {'list':dlist}
    
    return render(request, 'pboard2/list.html', context)
    
    # 딕셔너리
    # a = {'id':'aaa', 'pw':1111}
    # print(a['id'])
    
def view(request, galContentId):
    global dlist
    print('넘어온 galContentId : ',galContentId)
    print(dlist)
    context = {}
    for d in dlist:
        if d['galContentId'] == str(galContentId):
            context['dData'] = d
    return render(request, 'pboard2/view.html', context)