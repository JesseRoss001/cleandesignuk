from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 80}))

    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
