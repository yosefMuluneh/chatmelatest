from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('my-rooms/', views.room,name="my-rooms")
]