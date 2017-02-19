"""userProfiling URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from userPro import views as uv
from userProfiling import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', uv.homePage, name='homePage'),
    url(r'^search/$', uv.search, name='search'),
    url(r'^searchResult/$', uv.searchResult, name='searchResult'),
    url(r'^userPage/(\d+)$', uv.userPage, name='userPage'),
    url(r'^propertyPage/(\S+)$', uv.propertyPage, name='propertyPage'),


    url(r'^1/$', uv.test, name='test'),


    url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}, name='static'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
]


