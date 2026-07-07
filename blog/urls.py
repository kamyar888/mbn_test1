from django.urls import path
from . import views

urlpatterns = [
    path('blog_home/', views.blog_home, name="blog-home"),
    path('blog_home/search/',views.blog_search,name="search"),  
    path('blog_home/category/<str:cat_name>/',views.blog_home,name="category"),
    path('blog_single/post-<int:pid>/', views.blog_single, name="blog-single"),
    path('blog_home/<str:author_username>/',views.blog_home, name="author"),
    path('popularpost/',views.popularpost),
]