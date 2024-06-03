# admin.py

from django import forms
from django.contrib import admin
from .models import Post

class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

    class Media:
        js = ('ckeditor5/ckeditor.js', 'js/ckeditor_init.js')

class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ('title', 'timestamp')
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)
