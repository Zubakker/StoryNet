from django.shortcuts import render, get_object_or_404, redirect, HttpResponse

from django.urls import reverse
from django.conf import settings
from django.db.models import Max

# Create your views here.
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from json import dumps

from django.views.generic import (
        CreateView,
        DetailView,
        ListView,
        UpdateView,
        DeleteView,
)
import sys
sys.path.append('..')
from pages.models import MyUser
from .models import Post, Comment
from .forms import PostForm, CommentForm



class PostDetailView(DetailView):
    queryset = Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        this_post = Post.objects.get(id=self.kwargs['pk'])
        author_id = this_post.author_id

        context['link_back'] = reverse('author-detail', kwargs={'pk': author_id})
        story_author = this_post.author
        try:
            context['author_name'] = MyUser.objects.get(user_id=story_author.id).full_name
        except MyUser.DoesNotExist:
            context['author_name'] = story_author.username

        max_likes = this_post.comments.aggregate(Max('like_number'))['like_number__max']
        top_comment = this_post.comments.filter(like_number=max_likes).first()
        if top_comment:
            comment_author = top_comment.author
            try:
                top_comment.user_name = MyUser.objects.get(user_id=comment_author.id).full_name
            except MyUser.DoesNotExist:
                top_comment.user_name = comment_author.username
            top_comment.link = reverse('author-detail', kwargs={'pk': comment_author.id})
            context['top_comment'] = top_comment

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
        form.instance.text = form.instance.text.replace('<', '&lt').replace('>', '&gt')
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    queryset = Post.objects.all()
    form_class = PostForm
    template_name = 'posts/post_create.html'

class PostCommentsCreateView(CreateView):
    queryset = Post.objects.all()
    queryset2 = MyUser.objects.all()
    form_class = CommentForm
    template_name = 'posts/post_comments_create.html'

    def get(self, request, **kwargs):
        args = self.request.GET.urlencode().split('=')
        if len(args) == 1:
            return super().get(request, **kwargs)
        
        if args[0] == 'like':
            comment_id = args[1]
            post_obj = Post.objects.get(id=self.kwargs['pk'])
            comments_queryset = post_obj.comments.all()
            try:
                comment_obj = comments_queryset.get(id=comment_id)
                try:
                    comment_obj.who_liked.get(id=request.user.id)
                    comment_obj.like_number -= 1
                    comment_obj.who_liked.remove(request.user)

                except Exception as ex:
                    comment_obj.like_number += 1
                    comment_obj.who_liked.add(request.user)
                comment_obj.save()
                return HttpResponse('{"success": "success"}')

            except Comment.DoesNotExist:
                return HttpResponse('{"error": "comment_not_found"}')

        if args[0] == 'page':
            post_obj = Post.objects.get(id=self.kwargs['pk'])
            comments_queryset = post_obj.comments.all()

            pages = Paginator(comments_queryset, 10)
            page_num = int(args[1])
            if page_num > pages.num_pages:
                return HttpResponse('{"error": "page_num_limit_exceeded"}')
            return_page = pages.page(page_num)
            return_list = list()
            for obj in return_page:
                obj_text = obj.text.split()
                return_item = dict()
                author = obj.author
                try:
                    return_item['author'] = MyUser.objects.get(user_id=author.id).full_name
                except MyUser.DoesNotExist:
                    return_item['author'] = author.username
                return_item['text'] = obj.text
                return_item['url'] = reverse('author-detail', kwargs={'pk': author.id})
                return_item['id'] = obj.id
                return_item['created_at'] = str(obj.created_at)
                return_item['like_number'] = obj.like_number
                try:
                    obj.who_liked.get(id=self.request.user.id)
                    return_item['ILiked'] = True
                except Exception as ex:
                    return_item['ILiked'] = False 
                return_list.append(return_item)
            return HttpResponse(dumps(return_list), content_type="application/json")



    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.like_number = 0
        form.instance.text = form.instance.text.replace('<', '&lt').replace('>', '&gt')

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_obj = Post.objects.get(id=self.kwargs['pk'])
        comments_queryset = post_obj.comments.all()

        pages = Paginator(comments_queryset, 10)
        return_page = pages.page(1)

        for comment in return_page:
            author = comment.author 
            comment.link = reverse('author-detail', kwargs={'pk': author.id})
            try:
                comment.author_name = MyUser.objects.get(user_id=author.id).full_name
            except MyUser.DoesNotExist:
                comment.author_name = author.username
            try:
                comment.who_liked.get(id=self.request.user.id)
                comment.ILiked = True
            except Exception as ex:
                comment.ILiked = False 


        context['comments'] = return_page
        context['comments_url'] = reverse('posts:post-comments', kwargs={'pk': self.kwargs['pk']})
        context['link_back'] = reverse('posts:post-details', kwargs={'pk': self.kwargs['pk']})
        author = self.request.user
        try:
            context['user_name'] = MyUser.objects.get(user_id=author.id).full_name
        except MyUser.DoesNotExist:
            context['user_name'] = author.username
        return context

    def get_success_url(self):
        post_obj = Post.objects.get(id=self.kwargs['pk'])
        post_obj.comments.add(self.object)
        return reverse('posts:post-comments', kwargs={'pk': self.kwargs['pk']})


