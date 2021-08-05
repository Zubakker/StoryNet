from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 

# Create your views here.
from django.core.exceptions import ValidationError

from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView,
)
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    def get_queryset(self, **kwargs):
        queryset = Post.objects.filter(author_id=self.request.user.id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['absolute_create_url'] = reverse('posts:post-create')
        return context

class PostDetailView(DetailView):
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['absolute_list_url'] = reverse('posts:post-list')
        return context

class PostDeleteView(DeleteView):
    queryset = Post.objects.all()
    def get_success_url(self):
        return reverse('posts:post-list')

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        if not pk:
            return
        if self.queryset.get(id=pk).author.id != self.request.user.id:
            raise ValidationError('Post author and current user dont match')
        return super().delete(self, pk)

class PostCreateView(CreateView):
    queryset = Post.objects.all()
    form_class = PostForm
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    form_class = PostForm
    template_name = 'posts/post_create.html'

