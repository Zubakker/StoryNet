from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
from .forms import PostForm, RawPostForm

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Home </h1>')
    return render(request, 'pages/home.html', {})

def author_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Hello </h1>')
    my_context = {
            'my_text': 'author rocks',
            'my_number': 796549,
            'my_list': [1, 2, 3, 4],
         }

    return render(request, 'pages/author.html', my_context)

def drafts_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Drafts </h1>'
    return render(request, 'pages/drafts.html', {})

def post_view(request, *args, **kwargs):
    obj = Post.objects.get(id=1)
    context = {
            'object': obj,
    }
    return render(request, 'pages/post.html', context )

def post_create_view(request, *args, **kwargs):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form,
    }
    return render(request, 'pages/post_create.html', context)

def post_edit_view(request, id, *args, **kwargs):
    form = PostForm(id=id)
    context = {
        'form': form,
    }
    return render(request, 'pages/post_create.html', context)


def messages_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Messages </h1>'
    return render(request, 'pages/messages.html', {})

def news_view(request, *args, **kwargs):
    #return HttpResponse('<h1> News </h1>'
    return render(request, 'pages/news.html', {})

def auth_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Auth </h1>'
    return render(request, 'pages/auth.html', {})
