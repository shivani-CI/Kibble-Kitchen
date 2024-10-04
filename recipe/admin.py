""" Admin module for managing Django admin portal """
from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, MealPlan, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """ Class for recipe admin """
    list_display = ['title', 'difficulty', 'status', 'created_at']
    search_fields = ['title', 'description']
    list_filter = ['status', 'created_at']
    summernote_fields = ['description']


@admin.register(Ingredient)
class IngredientAdmin(SummernoteModelAdmin):
    """ Class for ingredient admin """
    list_display = ['name']
    search_fields = ['name']


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(SummernoteModelAdmin):
    """ Class for recipe ingredient admin """
    list_display = ['recipe', 'ingredient', 'quantity', 'unit']
    search_fields = ['recipe', 'ingredient']


@admin.register(MealPlan)
class MealPlanAdmin(SummernoteModelAdmin):
    """ Class for meal plan admin"""
    list_display = ['title', 'start_date', 'end_date', 'created_at']
    search_fields = ['title']


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    """ Class for comment admin"""
    list_display = ['recipe', 'user', 'body', 'created_at']
    search_fields = ['recipe', 'user']
    list_filter = ['approved', 'created_at']
    summernote_fields = ['body']
