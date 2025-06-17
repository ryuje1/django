from django.shortcuts import render
import requests
import json

# 공공데이터 리스트 
def list(request):
    dlist = publicData()
    context = {'list':dlist}
    return render(request, 'pboard/list.html', context)


# 공공데이터 상세보기 - 공공데이터 다시 호출
def view(request, galContentId):
    print('넘어온 galContentId : ', galContentId)
    # 공공데이터 호출
    dlist = publicData()
    dData = {}
    
    for d in dlist:
        if d['galContentId'] == str(galContentId):  # 타입확인
            print('검색된 데이터 : ', d)
            dData = d
            break
        
    context = {'dData':dData}
    return render(request, 'pboard/view.html', context)


def publicData():
    public_key = 'bL05ehIVxrekLZkNPfKKTOw%2FG6cS1dFlgNuQS5K5hlHUuHGQn3MZAJ7GxH0IbYTxX4D5FPl6XzogD7CBxyrJyg%3D%3D'
    pageNo = 1
    url = f'http://apis.data.go.kr/B551011/PhotoGalleryService1/galleryList1?serviceKey={public_key}&numOfRows=10&pageNo={pageNo}&MobileOS=ETC&MobileApp=AppTest&arrange=A&_type=json'
    # 웹스크래핑 requests
    response = requests.get(url)
    # print("공공데이터 : ", response.text)   # str타입
    
    # 문자열 -> json 타입으로 변경
    json_data = json.loads(response.text)
    dlist = json_data['response']['body']['items']['item']
    # print('json 데이터 : ', json_data['response']['body']['items']['item'])     # json타입
    # print('json 데이터 1개 : ', json_data['response']['body']['items']['item'][0])
    
    return dlist