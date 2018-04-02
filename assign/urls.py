"""assign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include,url
from django.contrib import admin
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib import auth
from login.login_forms import LoginForm
from login.register_forms import RegisterForm

# urlpatterns = [
#     url(r'^admin/', admin.site.urls),
#     url(r'^login/$', auth_views.login, render('login.html', 'home'), name='login'),
#     url(r'^logout/$',auth_views.logout, render('logout.html', 'home'), name='logout'),
#     url(r'', include('login.urls')),
#     #url(r'', include('password_reset.urls')),
#     url(r'', include('django.contrib.auth.urls')),
#     url(r'^password_reset/$', auth_views.password_reset,render('password_reset', 'password_reset'), name='password_reset'),
#     url(r'^password_reset/done/$', auth_views.password_reset_done,render('password_reset_done', 'password_reset')),
#     url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
#     auth_views.password_reset_confirm,render('password_reset_confirm', 'password_reset')),
#     url(r'^reset/done/$', auth_views.password_reset_complete,render('password_reset_complete', 'password_reset')),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, {'template_name': 'home/login.html'}, name='login'),
    url(r'^logout/$',auth_views.logout,{'template_name': 'home/logout.html'}, name='logout'),
    url(r'', include('login.urls')),
    url(r'', include('django.contrib.auth.urls')),
    # url(r'^password_reset/$', auth_views.password_reset,{'template_name': 'registraion/password_reset.html'}, name='password_reset'),
    # url(r'^password_reset/done/$', auth_views.password_reset_done,{'template_name': 'registration/password_reset_done.html'}),
    # url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    # auth_views.password_reset_confirm,{'template_name': 'registration/password_reset_confirm.html'}),
    # url(r'^reset/done/$', auth_views.password_reset_complete,{'template_name': 'registration/password_reset_complete.html'}),
]