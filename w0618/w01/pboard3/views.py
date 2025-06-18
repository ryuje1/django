from django.shortcuts import render
import requests
import json

mlist = []

def list(request):
    global mlist
    serviceKey = '844d770ee2d8d1243a078a1d2678f769'
    url = f'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={serviceKey}&targetDt=20250617'
    
    response = requests.get(url)
    json_data = json.loads(response.text)
    mlist = json_data['boxOfficeResult']['dailyBoxOfficeList']
    print('전체 데이터 : ', mlist)
    
    context = {'list':mlist}
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