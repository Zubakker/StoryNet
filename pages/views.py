from django.shortcuts import render, get_object_or_404
from django.urls import reverse 

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.views.generic import (
        CreateView,
        UpdateView, View,
        DetailView,
        FormView,
)
import sys
sys.path.append("..")
from posts.models import Post, MyUser


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

def messages_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Messages </h1>'
    return render(request, 'pages/messages.html', {})

def news_view(request, *args, **kwargs):
    #return HttpResponse('<h1> News </h1>'
    return render(request, 'pages/news.html', {})

def auth_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Auth </h1>'
    return render(request, 'pages/auth.html', {})

class RegisterView(CreateView):
    queryset = User.objects.all()
    form_class = UserCreationForm 
    template_name = 'registration/register.html'
    c_username = ''


    def form_valid(self, form):
        self.c_username = form.cleaned_data['username']
        return super().form_valid(form)


    def get_success_url(self, *args, **kwargs):
        c_user_id = User.objects.get(username=self.c_username).id
        connected_myuser = MyUser(user_id=c_user_id)
        connected_myuser.save()
        success_url = reverse('login')
        return success_url

class AuthorDetailView(DetailView):

    queryset = User.objects.all()
    def get_queryset(self, **kwargs):
        self.posts_queryset = Post.objects.filter(author_id=self.request.user.id)
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


