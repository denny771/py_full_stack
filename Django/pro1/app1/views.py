from django.shortcuts import render
from django.http import HttpResponse
from app1.models import Topic,Webpage,AccessRecord
# import models
# Create your views here.

# def index(request):
    # return HttpResponse("ndex")

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'acess_records':webpages_list}
    
    return render(request,'app1/help.html',context=date_dict)