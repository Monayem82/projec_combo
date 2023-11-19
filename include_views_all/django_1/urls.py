from django.urls import path
from . import views

urlpatterns = [
    path('dd1/',views.homePage,name='homes'),
    path('ddd2/',views.dj,name='dj2page')
]
