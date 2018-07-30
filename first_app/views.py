from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from .logic import show

# Create your views here.
def index(request):
    
    number=int(4)
    if request.method=="POST":
        form=ContactForm(request.POST)
        if form.is_valid():

            
            number=form.cleaned_data['number']
    result=show(number)
    form=ContactForm()
    return render(request,'first_app/index.html',{'form':form,'result':result})    

