# blog/urls.py
from django.urls import path
from . import views

app_name = 'blog' # Namespace for your app's URLs

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
]