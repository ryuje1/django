from django.urls import path, include
from . import views

app_name = 'photocard'
urlpatterns = [
    path('exchange/', views.exchange, name="exchange"),
    path('detail/', views.detail, name="detail"),
    path('recent/', views.recent, name="recent"),
]
