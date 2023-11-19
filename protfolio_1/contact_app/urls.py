from django.urls import path
from . import views
urlpatterns = [
    path('contact/',views.contactHome,name='contactpages'),
    path('gallary/',views.gallaryView,name='gallary'),
    path('tempareture/',views.tempareture,name='tempareture'),

]
