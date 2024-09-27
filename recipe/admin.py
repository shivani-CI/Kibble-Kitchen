from recipe.models import Recipe, Ingredient, RecipeIngredient, MealPlan, Comment 
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ['title', 'difficulty' ,'status', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['status', 'created_at']
    summernote_fields = ['description']


@admin.register(Ingredient)
class IngredientAdmin(SummernoteModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(SummernoteModelAdmin):
    list_display = ['recipe', 'ingredient', 'quantity', 'unit']
    search_fields = ['recipe', 'ingredient']


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ['recipe', 'user', 'body', 'created_at']
    search_fields = ['recipe', 'user']
    list_filter = ['approved', 'created_at']
    summernote_fields = ['body']
    