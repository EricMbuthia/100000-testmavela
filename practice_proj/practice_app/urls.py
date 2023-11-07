from django.urls import path
from practice_app import views

urlpatterns = [
path('', views.home, name='home'),

path('home/', views.home, name='home'),

]
