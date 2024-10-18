from django.shortcuts import render
from . import forms as f
from . import models as m

def get_posts(request):
    posts = m.Post.objects.all()
    
    return render(request, 'blog/posts.html', {'posts': posts})
