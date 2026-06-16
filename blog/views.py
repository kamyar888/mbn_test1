from django.shortcuts import render , get_object_or_404
from blog.models import Post 
def blog_home(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    posts = get_object_or_404(posts, id=pid ,status=1)
    posts.counted_views += 1
    posts.save()
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html',context) 
def test(request):
    return render(request, 'blog/test.html')
def popularpost(request):
    return render(request, 'popularpost.html')

# Create your views here.
