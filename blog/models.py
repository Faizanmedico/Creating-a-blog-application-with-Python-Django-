from django.db import models

# Create your models here.
# blog/models.py
from django.db import models
from django.contrib.auth.models import User # To link posts to users

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories" # Fixes plural in admin

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = (
        (0, "Draft"),
        (1, "Published"),
    )
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True) # For SEO-friendly URLs
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    class Meta:
        ordering = ['-created_on'] # Order posts by creation date, newest first

    def __str__(self):
        return self.title