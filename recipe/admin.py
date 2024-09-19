from django.contrib import admin
from .models import Recipe, Comment, Ingredient
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'difficulty' ,'status', 'created_at')
    search_fields = ['title', 'description']
    list_filter = ('status', 'created_at',)
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):

    list_display = ('user_id', 'body', 'created_at')
    search_fields = ['recipe_id', 'user_id']
    list_filter = ('approved', 'created_at',)
    summernote_fields = ('body',)


# Register your models here.
admin.site.register(Ingredient)
