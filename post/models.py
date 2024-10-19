from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    Status_choices = [
        ('Draft','DR'),
        ('Published',   'PB')
    ]
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='default.png')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    published_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=Status_choices, null=True, max_length=50)
    tags = models.ManyToManyField('Tag', related_name='posts')
    views = models.IntegerField(default=0)  # Ko'rishlar soni uchun maydon

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:100]

class PostReview(models.Model):
    title = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Sharh muallifi
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reviews', null=True, blank=True)  # Postga bog'lanish
    comment = models.TextField()  # Sharh mazmuni
    created_at = models.DateTimeField(default=timezone.now)  # Sharh yaratilgan sana

    def __str__(self):
        
        return f"Review by {self.author} on {self.title}"
