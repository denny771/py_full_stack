from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(requests):
    my_dict = {'insert_me': "Help page"}
    return render(requests, 'first_app/index.html', context=my_dict)
    # return render(requests, 'first_app//')