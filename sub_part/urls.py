from django.urls import path,include
from sub_part import views

urlpatterns=[
    path('',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('home',views.index,name='home'),
]