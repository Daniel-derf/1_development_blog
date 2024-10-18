from django.shortcuts import render

# Create your views here.

def get_posts(request):
    return render(request, 'blog/posts.html')
