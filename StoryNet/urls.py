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
from django.urls import path

from pages.views import home_view, author_view, drafts_view, post_view,\
        messages_view, news_view, auth_view, post_create_view, \
        post_edit_view

urlpatterns = [
    path('', home_view),
    path('author/', author_view),
    path('drafts/', drafts_view),
    path('post/', post_view),
    path('post/<int:id>', post_edit_view),
    path('post_create/', post_create_view),
    path('messages/', messages_view),
    path('news/', news_view),
    path('auth/', auth_view),
    path('admin/', admin.site.urls),
]
