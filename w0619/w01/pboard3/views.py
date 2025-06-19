from django.shortcuts import render
from django.http import JsonResponse
import requests
import json

mlist = []

def list(request):
    # 공통영역 : 영화데이터 호출
    context = publicScreen('20250617')
    return render(request, 'pboard3/list.html', context)

def view(request, rank):
    global mlist
    print('mlist : ', mlist)
    print('rank : ', rank)
    context = {}
    
    for m in mlist:
        if m['rank'] == str(rank):
            context['mdata'] = m
    print('context : ', context)
    
    return render(request, 'pboard3/view.html', context)


# ajax통신 - 리턴타입 JsonResponse
def searchAjax(request):
    ## 영화 데이터 가져오기
    targetDt = request.POST.get('searchInput', '20250617')
    print('targetDt : ', targetDt)
    serviceKey = '844d770ee2d8d1243a078a1d2678f769'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={serviceKey}&targetDt={targetDt}'
    
    response = requests.get(url)
    json_data = json.loads(response.text)
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    print('전체 데이터 : ', mlist)
    
    context = {'list':mlist}
    
    return JsonResponse(context)

# 공통영역 : 영화데이터 가져오기 함수
def publicScreen(targetDt):
    global mlist
    serviceKey = '844d770ee2d8d1243a078a1d2678f769'
    targetDt = '20250617'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={serviceKey}&targetDt={targetDt}'
    
    response = requests.get(url)
    json_data = json.loads(response.text)
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    print('전체 데이터 : ', mlist)
    
    context = {'list':mlist}
    return context