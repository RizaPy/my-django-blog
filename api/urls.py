from django.urls import path
from .views import ListPostAPIView

urlpatterns = [
    path('api-posts/', ListPostAPIView.as_view(), name='api_posts'),
]
