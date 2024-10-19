
from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from post.models import Post, Category

def home(request):
    # So'nggi yangiliklar (oxirgi 5 ta post)
    latest_news = Post.objects.all().order_by('-created_at')[:5]

    # Eng ko'p o'qilgan postlar (umumiy)
    most_read_posts = Post.objects.all().order_by('-views')[:5]

    # Oxirgi haftada eng ko'p o'qilganlar
    one_week_ago = timezone.now() - timedelta(days=7)
    most_read_week = Post.objects.filter(created_at__gte=one_week_ago).order_by('-views')[:5]

    # Oxirgi oyda eng ko'p o'qilganlar
    one_month_ago = timezone.now() - timedelta(days=30)
    most_read_month = Post.objects.filter(created_at__gte=one_month_ago).order_by('-views')[:5]

    # Kategoriyalar va ularning postlari
    categories = Category.objects.prefetch_related('posts')

    context = {
        'latest_news': latest_news,
        'most_read_posts': most_read_posts,
        'most_read_week': most_read_week,
        'most_read_month': most_read_month,
        'categories': categories,
    }

    return render(request, 'home.html', context)
    