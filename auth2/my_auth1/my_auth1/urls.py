"""my_auth1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import RedirectView
#from .views import redirect_main
from two_factor.urls import urlpatterns as tf_urls

from django.contrib.auth.views import LoginView
from django_otp.forms import OTPAuthenticationForm




urlpatterns = [
   #path('', redirect_main),
    path('admin/', admin.site.urls),
    path('authsys1app/', include('authsys1app.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    #path('login/', LoginView.as_view(authentication_form=OTPAuthenticationForm)),
    path('', RedirectView.as_view(url='/authsys1app/', permanent=True)),
    #path(r'', include(tf_urls)),

    #path(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
]


