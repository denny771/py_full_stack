from django.urls import include, re_path, path
from first_app import views

urlpatterns = [
    re_path(r'^$',views.help,name='help')
]

