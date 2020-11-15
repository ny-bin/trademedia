from django import forms
from .models import Content

class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    picture = forms.ImageField()
