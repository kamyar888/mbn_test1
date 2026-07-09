from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact
from django.contrib import messages
from website.form import NameForm
def Index_views(request):
    return render(request, 'website/index.html')

def About_views(request):
    return render(request, 'website/about.html')

def ContactUs_views(request):
    return render(request, 'website/contact.html')

def test_views(request):
    form = NameForm()  
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            print(name,subject,email,message)
            return HttpResponse('done')
          
    return render(request, 'test.html',{'form': form})  