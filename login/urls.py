from django.conf.urls import url
from django.contrib import admin
from .views import home,register,logins

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^register/', register, name="register"),
]
