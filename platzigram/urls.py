from django.contrib import admin
from django.urls import path

from posts import views as posts_views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('posts/', posts_views.list_posts),
]
