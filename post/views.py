from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

from post.models import Post, Category, PostReview
from post.forms import PostForm, PostReviewForm

class PostListView(View):
    def get(self, request):

        categories = Category.objects.all()
        posts = Post.objects.all().order_by('-published_time')
        reviews = PostReview.objects.all()
        latest_posts = Post.objects.all().filter()[:5]

        search_query = request.GET.get('q')
        if search_query:
            posts = posts.filter(title__icontains=search_query)

        paginator = Paginator(posts, 5)

        page_num = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_num)
        context = {
            'page_obj':page_obj,
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
    


def post_create_view(request):
    if request.method=='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.is_approved = False  # Post tasdiqlanmagan holda saqlanadi
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form':form})


class AddReviewView(LoginRequiredMixin, View):
    def post(self, request, id):
        post = Post.objects.get(id=id)
        review_form = PostReviewForm(data=request.POST)
        if review_form.is_valid():
            PostReview.objects.create(
                        post=post,
                        author = request.user,
                        comment = review_form.cleaned_data['comment']
            )
            return redirect(reverse('post_detail', kwargs ={'id':id}))
        return render(request, 'detail_post.html', {'post':post, 'review_form':review_form})