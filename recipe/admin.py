from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'difficulty' ,'status', 'created_at')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_at',)
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Comment)