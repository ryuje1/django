from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('list/', views.list, name='list'),     
    path('view/', views.view, name='view'),        # 1. form 데이터 전송
    path('view2/', views.view2, name='view2'),     # 2. ajax 데이터 전송 
]