from django import forms
from .models import Post


class MessageForm(forms.ModelForm):

    class Meta:
        model=Post
        fields=['name','title','message']