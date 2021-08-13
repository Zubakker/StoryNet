from django import forms

from .models import Post, Genre, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
             'title',
             'epigraph',
             'epigr_author',
             'text',
             'genres',
             'summary',
             'like_number',
        ]
        widgets = {
            'summary': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'text',
        ]
        widgets = {
                'text': forms.Textarea(attrs={'class': 'comment_text'}),
        }

