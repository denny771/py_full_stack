from django.shortcuts import render
from basicapp import forms
# Create your views here.

def index(request):
    return render(request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation sucess")
            cred = ['name','email','text']
            for i in cred:
                print(form.cleaned_data[i])

    return render(request,'basicapp/form_page.html',{'form':form})
    