from django.shortcuts import render, get_object_or_404, HttpResponse
from django.urls import reverse 

from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.views.generic import (
        CreateView,
        UpdateView, View,
        DetailView,
        FormView,
        ListView,
)
from json import dumps

import sys
sys.path.append("..")
from posts.models import Post
from .models import MyUser
from .forms import AuthorForm


# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse('<h1> Home </h1>')
    return render(request, 'pages/home.html', {})

class RegisterView(CreateView):
    queryset = User.objects.all()
    form_class = UserCreationForm 
    template_name = 'registration/register.html'
    c_username = ''


    def form_valid(self, form):
        self.c_username = form.cleaned_data['username']
        return super().form_valid(form)


    def get_success_url(self, *args, **kwargs):
        print(self.c_username)
        c_user_id = User.objects.get(username=self.c_username).id
        connected_myuser = MyUser(user_id=c_user_id)
        connected_myuser.save()
        success_url = reverse('login')
        return success_url


class AuthorDetailView(DetailView):
    queryset = MyUser.objects.all()
    template_name = 'pages/author_detail.html'
    def get(self, request, **kwargs):
        post_queryset = Post.objects.filter(author_id=self.kwargs['pk'])

        pages = Paginator(post_queryset, 50)
        page_num = self.request.GET.urlencode().split('=')
        if page_num[0]:
            if int(page_num[1]) > pages.num_pages:
                return HttpResponse('{"error": "page_num_limit_exceeded"}')
            return_page = pages.page(int(page_num[1]))
            return_list = list()
            for obj in return_page:
                obj_text = obj.text.split()
                return_item = dict()
                return_item['title'] = obj.title
                return_item['url'] = reverse('posts:post-details', kwargs={'pk': obj.id})
                if len(obj_text) > 40:
                    return_item['text'] = ' '.join(obj_text[:40])
                    return_item['long'] = True
                else:
                    return_item['text'] = obj_text
                    return_item['long'] = False
                return_list.append(return_item)
            return HttpResponse(dumps(return_list), content_type="application/json")
        else:
            return super().get(request, **kwargs)

    def get_queryset(self, **kwargs):
        return self.queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_queryset = Post.objects.filter(author_id=self.kwargs['pk'])

        pages = Paginator(post_queryset, 50)
        return_page = pages.page(1)

        for obj in return_page:
            obj_text = obj.text.split()
            obj.url = reverse('posts:post-details', kwargs={'pk': obj.id})
            if len(obj_text) > 40:
                obj.text = ' '.join(obj_text[:40])
                obj.long = True
            else:
                obj.long = False
            

        context['post_queryset'] = return_page
        context['this_page_url'] = reverse('author-detail', kwargs={'pk': self.kwargs['pk']})
        return context


class AuthorUpdateView(UpdateView):
    queryset = MyUser.objects.all()
    template_name = 'pages/author_update.html'
    form_class = AuthorForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    

class AuthorSearchView(ListView):
    queryset = MyUser.objects.all()
    template_name = 'pages/author_search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = self.queryset.filter(full_name=query)
        print(object_list)
        return object_list

