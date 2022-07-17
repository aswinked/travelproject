from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    #path('result/',views.result,name='result'),
    #path('add/',views.substraction,name='substraction'),
   # path('add/',views.multiplication,name='multiplication'),


   # path('contact/',views.contact,name='contact')
]
