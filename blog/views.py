from django.shortcuts import render
from django.http import JsonResponse
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


def delete_post(request, id):
    selected_client = m.Post.objects.filter(id=id)
    response = f"Post de id {str(id)} "
    if selected_client:
        selected_client.delete()
        response += "deletado com sucesso!"
    else:
        response += "não existente."
    return JsonResponse({'res': response})