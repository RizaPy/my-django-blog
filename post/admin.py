from django.contrib import admin
from post.models import Tag, Category, Post, PostReview

# admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(PostReview)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'is_approved')
    list_filter = ('is_approved', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)