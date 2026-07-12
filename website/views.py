from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from website.form import ContactForm, NewsLetterForm
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
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully!')
        else:
            messages.add_message(request, messages.ERROR, 'Please correct the errors below.')
        return render(request, 'website/contact.html', {"form": form})
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {"form": form})

def newsletter_views(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'You have successfully subscribed to our newsletter!')
        else:
            messages.add_message(request, messages.ERROR, 'Please enter a valid email address.')
        return HttpResponseRedirect(reverse('contact'))
    return HttpResponseRedirect(reverse('contact'))

def test_views(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  
        if form.is_valid():
            form.save()  
            return HttpResponse('Done')
    else:
        form = ContactForm()  
    return render(request, 'test.html', {'form': form})