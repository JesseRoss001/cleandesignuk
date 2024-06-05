from django.contrib import admin
from .models import Template, Component

class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)

class ComponentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'description')
    readonly_fields = ('created_at',)

admin.site.register(Template, TemplateAdmin)
admin.site.register(Component, ComponentAdmin)
