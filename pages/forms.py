from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author',
            'title',
            'epigraph',
            'text',
        ]

class RawPostForm(forms.Form):
    author      = forms.CharField()
    title       = forms.CharField(required=False)
    epigraph    = forms.CharField()
    text        = forms.CharField(widget=forms.Textarea(
                            attrs={
                                'rows': 20,
                                'cols': 100,
                            }
                        )
                  )


