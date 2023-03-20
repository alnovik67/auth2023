from django.urls import path
from .views import *


urlpatterns = [

    path('', index, name='index'),
    path('user1page/', User1page.as_view(), name='User1page'),
    path('user2page/', User2page.as_view(), name='User2page'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]