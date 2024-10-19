from django.urls import path
from .views import PostListView, PostDetailView, post_create_view

urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("<int:id>/", PostDetailView.as_view(), name="post_detail"),
    path('create/', post_create_view, name='create_post'),
    
]