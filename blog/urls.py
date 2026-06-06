from django.urls import path
from . import views

urlpatterns = [
    path('blog_home/', views.blog_home, name="blog-home"),
    path('blog_single/post-<int:pid>/', views.blog_single, name="blog-single"),
    path('test/post-<int:pid>/', views.test, name="test"),
]