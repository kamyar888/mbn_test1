from django.shortcuts import render, get_object_or_404
from blog.models import Post 
from django.core.paginator import Paginator ,PageNotAnInteger , EmptyPage

def blog_home(request, cat_name=None, author_username=None):
    posts = Post.objects.filter(status=1) 
    if cat_name:
        posts = posts.filter(category__name=cat_name)
    elif author_username:
        posts = posts.filter(author__username=author_username)   
    posts = Paginator(posts , 4)    
    try :
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage :
        posts = posts.get_page(1)    
    context = {
        'posts': posts,
        'author_username': author_username,  
    }
    return render(request, 'blog/blog-home.html', context)
    
def blog_single(request, pid):
    posts = Post.objects.filter(status=1)
    posts = get_object_or_404(posts, id=pid, status=1)
    posts.counted_views += 1
    posts.save()
    context = {'posts': posts}
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request, 'blog/test.html')

def popularpost(request):
    return render(request, 'popularpost.html')

def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1, category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    query = request.GET.get('s')
    
    if query:
        posts = posts.filter(content__contains=query)
    
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context) 