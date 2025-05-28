from django.urls import path, include
from . import views

app_name = 'students'
urlpatterns = [
    path('list/', views.list, name='list'),
    path('write/', views.write, name='write'),  # write.html - GET, POST / 홈에서 write 페이지 이동 시 GET, write 페이지에서 저장 버튼 누르면 POST
    path('view/', views.view, name='view'),
    path('update/<str:name>/', views.update, name='update'),
    path('delete/<str:name>/', views.delete, name='delete'),
]