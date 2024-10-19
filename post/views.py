from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView

from post.models import Post, Category, PostReview
from post.forms import PostForm, PostReviewForm

class PostListView(View):
    def get(self, request):

        categories = Category.objects.all()
        posts = Post.objects.all().order_by('-published_time')
        reviews = PostReview.objects.all()
        latest_posts = Post.objects.all().filter()[:5]
        context = {
            'posts':posts,
            'latest_posts':latest_posts,
            'categories':categories,
            'reviews':reviews
        }
        return render(request, 'posts.html', context)

class PostDetailView(View):
    def get(self, request, id):
        post = Post.objects.get(id=id)
        review_form = PostReviewForm()
        context = {
            'post':post,
            'review_form':review_form,
        }
        return render(request, 'detail_post.html', context)
    
    def post(self, request, id):
        post = Post.objects.get(id=id)
        reviews = PostReview.objects.all()
        
        if request.method == "POST":
            review_form = PostReviewForm(request.POST)
            if review_form.is_valid():
                review_form.save(commit=False)
                review_form.post = post
                review_form.save()
                return redirect('post_detail', id=post.id)
        else:
            review_form = PostReviewForm()
        return render(request, 'detail_post.html', {'post':post, 'reviews':reviews, 'review_form':review_form})



def post_create_view(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form':form})


