from django.urls import path
from . import views

app_name='nike'

urlpatterns=[
    path('index',views.index, name='index'),
    path('find',views.find_store, name='find-store'),
    path('help',views.help, name='help'),
    path('join-us',views.join_us, name='join-us'),
    path('sign-in',views.sign_in, name='sign-in')
]    