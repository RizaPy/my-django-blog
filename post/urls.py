from django.urls import path
from .views import PostListView, PostDetailView, post_create_view, AddReviewView, EditReviewView, ConfirmDeleteReview, DeleteReviewView


urlpatterns = [
    path("", PostListView.as_view(), name="post"),
    path("<int:id>/", PostDetailView.as_view(), name="post_detail"),
    path("<int:review_id>/reviews/", AddReviewView.as_view(), name="reviews"),
    path("<int:post_id>/reviews/<int:review_id>/edit/", EditReviewView.as_view(), name="edit_review"),
    path("<int:post_id>/reviews/<int:review_id>/confirm/delete/", ConfirmDeleteReview.as_view(), name="confirm_delete_review"),
    path("<int:post_id>/reviews/<int:review_id>/delete/", DeleteReviewView.as_view(), name="delete_review"),
    path('create/', post_create_view, name='create_post'),
    
]
