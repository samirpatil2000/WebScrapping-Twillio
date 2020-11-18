from django.shortcuts import render
from .forms import Form
# Create your views here.
def ajax_home(request):
    form=Form()
    if request.method=="POST":
        form=Form(request.POST or None,request.FILES or None)
        if form.is_valid():
            form.save(commit=False)
            form.save()

    context={
        'form':form
    }

    return render(request,'scrapper/ajax_home.html',context)