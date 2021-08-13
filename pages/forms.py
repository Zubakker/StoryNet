from django import forms

from django.contrib.auth.models import User

from .models import MyUser

class AuthorForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = [
            'full_name',
            'contacts',
            'biography',
            'status',
            'photo',
        ]

