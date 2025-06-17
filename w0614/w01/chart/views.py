from django.shortcuts import render
from chart.models import TotalSales
from django.http import JsonResponse

# 차트 페이지 호출
def chlist(request):
    profit = [20, 15, 7, 25, 27, 30]
    context = {'profit':profit}
    print('영업이익 : ', profit)
    return render(request, 'chart/chlist.html', context)

def chlist2(request):
    return render(request, 'chart/chlist2.html')

def chlist3(request):
    return render(request, 'chart/chlist3.html')

# ajax으로 json타입으로 리턴
def chajax(request):
    aYear = request.POST.get('aYear')
    print('넘어온 aYear : ', aYear)
    # db 불러오기 - 하단 댓글때 qs 데이터를 list 타입으로 변경에서 리턴 - json파일로 변경돼서 넘어감
    qs = TotalSales.objects.filter(year=aYear)
    print('qs 기본구문 : ', qs)
    print('list 타입 구문 : ', list(qs.values()))
    
    # json 타입으로 변경
    context = {'ajaxlist':list(qs.values())}
    return JsonResponse(context)