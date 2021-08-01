from django.urls import path, include

from posts.views import (
        post_list_view,
        post_create_view,
        post_details_view,
        post_edit_view,
        post_delete_view,
)

app_name = 'posts'
urlpatterns = [
    path('list', post_list_view, name='post-list'),
    path('create', post_create_view, name='post-create'),
    path('<int:id>', post_details_view, name='post-details'),
    path('<int:id>/edit', post_edit_view, name='post-edit'),
    path('<int:id>/delete', post_delete_view, name='post-delete'),
]
