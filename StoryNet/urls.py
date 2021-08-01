"""StoryNet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from pages.views import (
        home_view, author_view, drafts_view, 
        messages_view, news_view, auth_view, 
)

urlpatterns = [
    path('post/', include('posts.urls')),

    path('', home_view, name='home'),
    path('author/<int:id>', author_view, name='author-by-id'),
    path('drafts/', drafts_view, name='drafts'),
    path('messages/', messages_view, name='messages'),
    path('news/', news_view, name='news'),
    path('auth/', auth_view, name='auth'),
    path('admin/', admin.site.urls, name='admin'),
]
