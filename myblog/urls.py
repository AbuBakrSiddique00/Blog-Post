from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pos/<str:pk>', views.pos, name="pos")
]