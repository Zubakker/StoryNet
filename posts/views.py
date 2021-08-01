from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse 

from .models import Post
from .forms import PostForm
# Create your views here.
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

def post_edit_view(request, id, *args, **kwargs):
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
