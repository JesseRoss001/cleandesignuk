from django.contrib import admin
from .models import Post
from .forms import PostForm

class PostAdmin(admin.ModelAdmin):
    form = PostForm
    list_display = ('title', 'slug', 'timestamp', 'updated_at')  # Fields to display in the list view
    search_fields = ('title', 'content')  # Fields to search in the admin panel
    list_filter = ('timestamp', 'updated_at')  # Filters for the right sidebar
    prepopulated_fields = {'slug': ('title',)}  # Automatically populate the slug field based on the title
    ordering = ('-timestamp',)  # Order posts by timestamp (most recent first)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content')
        }),
        ('SEO Fields', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Timestamps', {
            'fields': ('timestamp', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('timestamp', 'updated_at')  # Make timestamps read-only

admin.site.register(Post, PostAdmin)
