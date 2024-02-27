from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.

from blog.models import Post



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'author',
        'publish',
        'syntax',
        'status'
    )
    list_filter = (
        'status',
        'created',
        'publish',
        'author',
        'syntax',
    )
    # search_fields = ('title', )
    search_fields = (
        'title',
        'syntax',
        'body'
    )
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')

    fieldsets = [
       (
            "Title/Meta", {
                'fields': [
                    'title',
                    'slug',
                    'author',
                    'status',
                    'syntax',
                    'publish'
                ],
            },
       ),
       (
            'Content',
            {
                'fields': [
                    ('body'),
                ]
            }
       )
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE},
    }
