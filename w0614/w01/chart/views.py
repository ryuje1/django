from django.shortcuts import render
from chart.models import TotalSales

def chlist(request):
    profit = [19, 20, 21, 22, 23, 24]
    context = {'profit':profit}
    # profit = [20, 15, 7, 25, 27, 30]
    # qs = TotalSales.objects.filter(year=2025)
    # print('qs 기본구문 : ', qs)
    # print('list 타입 구문 : ', list(qs.values()))
    # context = {'profit':profit, 'list':qs, 'list_list':list(qs.values())}
    # print('영업이익 : ', profit)
    return render(request, 'chart/chlist.html', context)
