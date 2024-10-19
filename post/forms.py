from django import forms

from post.models import Post, PostReview

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'category', 'tags']

class PostReviewForm(forms.ModelForm):
    class Meta:
        model = PostReview
        fields = ['comment']