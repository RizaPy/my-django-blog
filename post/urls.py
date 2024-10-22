from django.urls import path
from .views import PostListView, PostDetailView, post_create_view, AddReviewView


urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("<int:id>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:id>/reviews/", AddReviewView.as_view(), name="reviews"),
    path('create/', post_create_view, name='create_post'),
    
]
