from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    # url(r'^home/$',views.home,name='home'),
    url(r'^about/$',views.about,name='about'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^signup/$',views.handleSignup,name='signup'),

] 