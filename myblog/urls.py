from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('pos/<str:pk>', views.pos, name="pos"),
    path('createPost', views.createPost, name="createPost"),
    path('editPost', views.editPost, name='editPost'),
    path('submit/<str:ps>', views.submit, name='submit'),
]