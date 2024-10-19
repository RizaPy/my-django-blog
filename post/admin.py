from django.contrib import admin
from post.models import Tag, Category, Post, PostReview

# admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(PostReview)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass