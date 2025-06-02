from django.urls import path, include
from . import views

app_name = 'board'
urlpatterns = [
    path('', views.list, name='list'),
    path('list/', views.list, name='list'),                 # 게시판 리스트
    path('write/', views.write, name='write'),              # 글 쓰기
    path('view/<int:bno>/', views.view, name='view'),        # 글 보기
    path('update/<int:bno>/', views.update, name='update'),  # 글 수정
]
