from django.contrib import admin
from django.urls import path

from blog import views as v

urlpatterns = [
    path('admin/', admin.site.urls),

    # POSTS
    path('posts/', v.get_posts),
    path('posts/detail/<int:id>/', v.get_post),
    path('posts/create/', v.create_post),
    path('posts/delete/<int:id>/', v.delete_post),

    # USERS

]
