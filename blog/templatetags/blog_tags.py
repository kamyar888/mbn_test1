from django import template
register = template.Library()

@register.simple_tag(name="Post_Counter")
def hello():
    from blog.models import Post  
    slam = Post.objects.filter(status=1).count()
    return slam
@register.simple_tag(name="posts")
def function(): 
    from blog.models import Post  
    posts = Post.objects.filter(status=1)
    return posts
@register.filter
def snip(value,args=20):
    return value[:args]
@register.inclusion_tag("blog/blog-popular-post.html")
def popularpost():
    from blog.models import Post
    posts = Post.objects.filter(status=1).order_by("-published_date")[:3]
    return {"posts":posts}
@register.inclusion_tag("blog/blog-post-categories.html")
def postcategories():
    from blog.models import category
    from blog.models import Post
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict} 
    