from django import template
register = template.Library()

@register.inclusion_tag("website/website_popular_post.html")
def popularpost():
    from blog.models import Post
    posts = Post.objects.filter(status=1).order_by("-published_date")[:7]
    from blog.models import category
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict={}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict, "posts":posts}