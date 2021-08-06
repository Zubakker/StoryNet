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
from django.conf.urls.static import static

from .settings import MEDIA_URL, MEDIA_ROOT

from pages.views import (
        home_view, drafts_view, 
        messages_view, news_view, auth_view, 
        RegisterView, AuthorDetailView,
        AuthorUpdateView,
)

urlpatterns = [
    path('post/', include('posts.urls')),

    path('', home_view, name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    # path('authorise/', AuthoriseView.as_view(), name='authorize'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('author/<int:pk>', AuthorDetailView.as_view(), name='author-by-id'),
    path('author/<int:pk>/update', AuthorUpdateView.as_view(), name='author-update'),
    path('drafts/', drafts_view, name='drafts'),
    path('messages/', messages_view, name='messages'),
    path('news/', news_view, name='news'),
    path('auth/', auth_view, name='auth'),
    path('admin/', admin.site.urls, name='admin'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
