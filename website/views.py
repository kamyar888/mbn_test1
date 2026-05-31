from django.shortcuts import render

def Index_views(request):
    return render(request, 'website/index.html')

def About_views(request):
    return render(request, 'website/about.html')

def ContactUs_views(request):
    return render(request, 'website/contact.html')

def test_views(request):
    return render(request, 'website/test.html')  