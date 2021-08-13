from django.urls import path, include

from posts.views import (
        PostDetailView,
        PostDeleteView,
        PostCreateView,
        PostUpdateView,
        PostCommentsCreateView,
)
'''
        post_list_view,
        post_create_view,
        post_details_view,
        post_edit_view,
        post_delete_view,
)
'''


app_name = 'posts'
urlpatterns = [
    path('create', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>', PostDetailView.as_view(), name='post-details'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('<int:pk>/comments', PostCommentsCreateView.as_view(), name='post-comments'),
]
'''
    path('list', post_list_view, name='post-list'),
    path('create', post_create_view, name='post-create'),
    path('<int:id>', post_details_view, name='post-details'),
    path('<int:id>/edit', post_edit_view, name='post-edit'),
    path('<int:id>/delete', post_delete_view, name='post-delete'),
]
'''
