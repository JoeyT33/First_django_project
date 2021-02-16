from django.urls import path     
from . import views

urlpatterns = [
    path('', views.home),
    path("blogs", views.showBlogs),
    path("blogs/new", views.new),
    path("blogs/create", views.create),
    path("blogs/<number>", views.show),
    path("blogs/<number>/edit", views.edit),
    path("blogs/<number>/delete", views.destroy)
]