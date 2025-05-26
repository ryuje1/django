from django.urls import path, include
from . import views

app_name = 'event'
urlpatterns = [
    path('list/', views.event, name='event'),   # http://127.0.0.1:8000/event/list/
]
