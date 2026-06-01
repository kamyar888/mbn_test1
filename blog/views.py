from django.shortcuts import render
from blog.models import Post 
def blog_home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html',context)
def test(request):
    return render(request, 'test.html')

# Create your views here.
