from django.urls import path
from practice_app import views

urlpatterns = [
path('home/', views.home, name='home')

]
