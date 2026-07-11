from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib import messages
from website.form import ContactForm , NewsLetterForm
from django.urls import reverse
def Index_views(request):
    return render(request, 'website/index.html')

def About_views(request):
    return render(request, 'website/about.html')

def ContactUs_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.ERROR,'its ok your message is send Func Its Worked')
        else:
                messages.add_message(request,messages.ERROR,'its ok your message is not send Func Its Worked')
        form = ContactForm()
    return render(request, 'website/contact.html')
def newsletter_views(request):
    form = NewsLetterForm(request.POST)
    if form.is_valid():
        form.save()
        messages.add_message(request,messages.SUCCESS,'its ok your NewsLetter Func Its Worked')
        return HttpResponseRedirect(reverse('contact'))
    else :
        messages.add_message(request,messages.ERROR,'its ok your NewsLetter Func Its Worked')
        return HttpResponse('ridi')
def test_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()  
            return HttpResponse('Done')
    
        form = ContactForm()  
    
    return render(request, 'test.html', {'form': form})