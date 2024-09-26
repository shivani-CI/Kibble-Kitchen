from django.contrib import admin
from .models import Recipe, Comment, RecipeIngredient, Ingredient
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


@admin.register(Ingredient)
class IngredientAdmin(SummernoteModelAdmin):

    list_display = ('ing_id', 'ing_name')
    search_fields = ['ing_name']


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(SummernoteModelAdmin):

    list_display = ('ing', 'quantity', 'unit')
    search_fields = ['ing']
    

# Register your models here.
# admin.site.register(MealPlan)
