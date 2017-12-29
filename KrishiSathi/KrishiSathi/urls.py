"""KrishiSathi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from app_krishisathi import views as krishi_views
from rest_framework.urlpatterns import format_suffix_patterns


if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^debug/', include(debug_toolbar.urls)),
        url(r'^$', krishi_views.show_homepage, name='home'),
        url(r'^signup/$', krishi_views.show_signup, name='signup'),
        url(r'^login/$', krishi_views.show_login, name='login'),
        url(r'^about/$', krishi_views.show_aboutpage, name='about'),
        url(r'^contact/$', krishi_views.show_contactpage, name='contact'),
        url(r'^logout/$', krishi_views.user_logout, name='user_logout'),
        #For Browsable Django-REST API:
        #url(r'^api/data', include('rest_framework.urls', namespace='rest_framework')),
        url(r'^api/data', krishi_views.User_DataList.as_view()),
        url(r'^api/users', krishi_views.User_InfoList.as_view()),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)