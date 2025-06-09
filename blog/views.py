from django.shortcuts import render

# Create your views here.
# blog/views.py
from django.shortcuts import render, get_object_or_404
from .models import Post, Category
from django.views import generic

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/index.html'
    paginate_by = 5 # Optional: for pagination

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

def category_posts(request, category_name):
    category = get_object_or_404(Category, name=category_name)
    posts = Post.objects.filter(category=category, status=1).order_by('-created_on')
    context = {
        'category': category,
        'posts': posts
    }
    return render(request, 'blog/category_posts.html', context)