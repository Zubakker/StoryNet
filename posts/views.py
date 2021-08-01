from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 

from .models import Post
from .forms import PostForm
from django.contrib.auth.models import User
# Create your views here.
'''
def post_list_view(request, *args, **kwargs):
    queryset = list(Post.objects.all())
    context = {
        'object_list': queryset,
        'absolute_create_url': reverse('posts:post-create'),
    }
    return render(request, 'posts/post_list.html', context)
    
def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('post-list'))
    context = {
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)

def post_details_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Post, id=id) 
    context = {
        'object': obj,
    }
    return render(request, 'posts/post_details.html', context)

def post_update_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Post, id=id) 
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect(reverse('post-list'))
    context = {
        'object': obj,
        'form': form,
    }
    return render(request, 'posts/post_create.html', context)

def post_delete_view(request, id, *args, **kwargs):
    obj = get_object_or_404(Post, id=id) 
    if request.method == 'POST':
        obj.delete()
        return redirect(reverse('post-list'))
    context = {
        'object': obj,
    }
    return render(request, 'posts/post_delete.html', context)
'''
from django.core.exceptions import ValidationError

from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView,
)

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
    #success_url = '/' #reverse('posts:post-list')
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

