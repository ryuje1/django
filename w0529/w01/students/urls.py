from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),
    path('writeOK/', views.writeOK, name='writeOK'),
    # html -> server 값 전달 1.파라미터 2.api방식 3.js  <str:name>
    path('view/<int:no>/', views.view, name='view'),
    path('update/<int:no>/', views.update, name='update'),   # 학생 정보 수정 페이지 열기
    path('updateOK/', views.updateOK, name='updateOK'), # 학생 정보 수정 완료
    path('delete/<int:no>/', views.delete, name='delete'), # 학생 정보 삭제
]