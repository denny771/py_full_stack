from django.urls import path , re_path , include

from appTwo import views

urlpatterns = [
    re_path(r'^$', views.users, name='users'),
]