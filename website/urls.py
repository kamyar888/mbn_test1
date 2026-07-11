from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index_views, name = "index"),
    path('about/', views.About_views , name = "about"),
    path('contact/', views.ContactUs_views , name = "contact"),
    path('test/', views.test_views , name = "test"),
    path('newsletter/', views.newsletter_views , name = "newsletter"),
]