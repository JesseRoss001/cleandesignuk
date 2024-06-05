from django.contrib import admin
from .models import Template, Component

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'intro')
    list_filter = ('created_at',)
    search_fields = ('name', 'intro', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {'fields': ('name', 'intro', 'description', 'price', 'image')}),
    )

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at', 'intro')
    list_filter = ('created_at',)
    search_fields = ('name', 'intro', 'description')
    readonly_fields = ('created_at',)
    fieldsets = (
        (None, {'fields': ('name', 'intro', 'description', 'price', 'image')}),
    )

admin.site.register(Template, TemplateAdmin)
admin.site.register(Component, ComponentAdmin)
