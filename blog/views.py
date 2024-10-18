from django.shortcuts import render
from . import forms as f
from . import models as m

def get_posts(request):
    posts = m.Post.objects.all()
    
    return render(request, 'blog/posts.html', {'posts': posts})

def get_post(request, id):
    post = m.Post.objects.filter(id=id).first()

    return render(request, 'blog/post_detail.html', {'post': post})

def create_post(request):
    context = {'form': f.PostForm()}
    if request.method == 'POST':
        form = f.PostForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            context = {'form': form}
    return render(request, "blog/create_post.html", context)